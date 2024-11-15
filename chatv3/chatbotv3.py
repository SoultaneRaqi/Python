import tensorflow as tf
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3
import pandas as pd
import numpy as np
import spacy
import requests
import json
import logging
import datetime
import threading
import queue
import os
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('chatbot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class Message:
    """Data class for message structure"""
    content: str
    timestamp: datetime.datetime
    sender: str
    intent: Optional[str] = None
    sentiment: Optional[float] = None
    entities: Optional[List[Dict]] = None

class Database:
    """Database management class"""
    def __init__(self, db_path: str = "chatbot.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize database tables"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    message TEXT,
                    response TEXT,
                    timestamp DATETIME,
                    intent TEXT,
                    sentiment FLOAT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS user_profiles (
                    user_id TEXT PRIMARY KEY,
                    name TEXT,
                    preferences TEXT,
                    last_interaction DATETIME
                )
            """)

    def store_conversation(self, user_id: str, message: Message, response: Message):
        """Store conversation in database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO conversations 
                (user_id, message, response, timestamp, intent, sentiment)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, message.content, response.content, 
                  message.timestamp, message.intent, message.sentiment))

class NLPProcessor:
    """Natural Language Processing class"""
    def __init__(self):
        # Load NLP models
        self.nlp = spacy.load("en_core_web_sm")
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.sentiment_model = AutoModelForSequenceClassification.from_pretrained(
            "finiteautomata/bertweet-base-sentiment-analysis"
        )
        self.vectorizer = TfidfVectorizer()

    def process_message(self, text: str) -> Message:
        """Process incoming message"""
        doc = self.nlp(text)
        
        # Extract entities
        entities = [
            {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char
            }
            for ent in doc.ents
        ]

        # Analyze sentiment
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.sentiment_model(**inputs)
        sentiment = float(tf.nn.softmax(outputs.logits)[0][1])

        return Message(
            content=text,
            timestamp=datetime.datetime.now(),
            sender="user",
            entities=entities,
            sentiment=sentiment
        )

class APIHandler:
    """External API integration handler"""
    def __init__(self):
        self.api_keys = self.load_api_keys()
        self.cache = {}
        self.cache_timeout = datetime.timedelta(minutes=5)

    def load_api_keys(self) -> Dict[str, str]:
        """Load API keys from environment variables"""
        return {
            "weather": os.getenv("WEATHER_API_KEY"),
            "news": os.getenv("NEWS_API_KEY"),
            "translation": os.getenv("TRANSLATION_API_KEY")
        }

    async def get_weather(self, location: str) -> Dict:
        """Get weather information"""
        cache_key = f"weather_{location}"
        if cache_key in self.cache:
            cached_time, cached_data = self.cache[cache_key]
            if datetime.datetime.now() - cached_time < self.cache_timeout:
                return cached_data

        url = f"https://api.weatherapi.com/v1/current.json"
        params = {
            "key": self.api_keys["weather"],
            "q": location
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        self.cache[cache_key] = (datetime.datetime.now(), data)
        return data

class ResponseGenerator:
    """Response generation class"""
    def __init__(self):
        self.load_response_templates()
        self.context_window = []
        self.max_context_length = 5

    def load_response_templates(self):
        """Load response templates from JSON"""
        with open("response_templates.json", "r") as f:
            self.templates = json.load(f)

    def generate_response(self, message: Message, context: List[Message]) -> Message:
        """Generate appropriate response"""
        # Update context window
        self.context_window.append(message)
        if len(self.context_window) > self.max_context_length:
            self.context_window.pop(0)

        # Generate response based on intent and context
        response_text = self.select_response_template(message)
        
        return Message(
            content=response_text,
            timestamp=datetime.datetime.now(),
            sender="bot"
        )

    def select_response_template(self, message: Message) -> str:
        """Select appropriate response template"""
        if message.intent in self.templates:
            templates = self.templates[message.intent]
            return np.random.choice(templates)
        return self.templates["default"][0]

class ChatBot:
    """Main chatbot class"""
    def __init__(self):
        self.db = Database()
        self.nlp_processor = NLPProcessor()
        self.api_handler = APIHandler()
        self.response_generator = ResponseGenerator()
        self.message_queue = queue.Queue()
        self.user_sessions = {}

    async def process_message(self, user_id: str, message_text: str) -> str:
        """Process incoming message and generate response"""
        try:
            # Process message
            message = self.nlp_processor.process_message(message_text)
            
            # Get user context
            context = self.user_sessions.get(user_id, [])
            
            # Generate response
            response = self.response_generator.generate_response(message, context)
            
            # Update context
            if user_id not in self.user_sessions:
                self.user_sessions[user_id] = []
            self.user_sessions[user_id].append(message)
            
            # Store conversation
            self.db.store_conversation(user_id, message, response)
            
            return response.content

        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            return "I apologize, but I encountered an error. Please try again."

    def run(self):
        """Run the chatbot"""
        print("Chatbot: Hello! I'm ready to chat. Type 'quit' to exit.")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                print("Chatbot: Goodbye!")
                break
            
            response = asyncio.run(self.process_message("user1", user_input))
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Initialize and run chatbot
    chatbot = ChatBot()
    chatbot.run()