import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import random
import json
import datetime
import re
from collections import deque

class AdvancedChatbot:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('punkt')
            nltk.download('stopwords')
            nltk.download('wordnet')
            nltk.download('averaged_perceptron_tagger')

        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.conversation_history = deque(maxlen=5)  # Keep last 5 exchanges
        self.user_name = None
        self.load_knowledge_base()
        
    def load_knowledge_base(self):
        # Knowledge base with categorized responses
        self.knowledge_base = {
            "greetings": {
                "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
                "responses": [
                    "Hello! How can I assist you today?",
                    "Hi there! What's on your mind?",
                    "Greetings! How may I help you?"
                ]
            },
            "farewells": {
                "patterns": ["bye", "goodbye", "see you", "take care"],
                "responses": [
                    "Goodbye! Have a great day!",
                    "Take care! Looking forward to our next chat!",
                    "Bye! It was nice talking to you!"
                ]
            },
            "gratitude": {
                "patterns": ["thank you", "thanks", "appreciate it"],
                "responses": [
                    "You're welcome!",
                    "Glad I could help!",
                    "My pleasure!"
                ]
            },
            "personal": {
                "patterns": ["what is your name", "who are you", "what can you do"],
                "responses": [
                    "I'm an advanced chatbot designed to help you with various tasks.",
                    "I'm your AI assistant, capable of understanding and responding to various queries.",
                    "I'm a chatbot with NLP capabilities, here to assist you!"
                ]
            }
        }

    def preprocess_text(self, text):
        """Preprocess text by tokenizing, removing stop words, and lemmatizing"""
        # Tokenize
        tokens = word_tokenize(text.lower())
        
        # Remove stop words and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token not in self.stop_words and token.isalnum()]
        
        return tokens

    def analyze_sentiment(self, text):
        """Analyze the sentiment of the input text"""
        analysis = TextBlob(text)
        
        # Get polarity (-1 to 1) and subjectivity (0 to 1)
        sentiment_score = analysis.sentiment.polarity
        
        if sentiment_score > 0.3:
            return "positive"
        elif sentiment_score < -0.3:
            return "negative"
        else:
            return "neutral"

    def extract_entities(self, text):
        """Extract named entities and important information"""
        # Basic entity extraction using regex
        entities = {
            'email': re.findall(r'[\w\.-]+@[\w\.-]+', text),
            'phone': re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text),
            'date': re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', text),
            'time': re.findall(r'\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)?', text)
        }
        return entities

    def generate_response(self, user_input):
        """Generate an appropriate response based on input analysis"""
        # Preprocess input
        tokens = self.preprocess_text(user_input)
        sentiment = self.analyze_sentiment(user_input)
        entities = self.extract_entities(user_input)
        
        # Update conversation history
        self.conversation_history.append({
            'user_input': user_input,
            'tokens': tokens,
            'sentiment': sentiment,
            'entities': entities,
            'timestamp': datetime.datetime.now()
        })
        
        # Check for user name if not already known
        if not self.user_name:
            name_match = re.search(r'my name is (\w+)', user_input.lower())
            if name_match:
                self.user_name = name_match.group(1).capitalize()
                return f"Nice to meet you, {self.user_name}! How can I help you today?"
        
        # Generate contextual response
        for category, data in self.knowledge_base.items():
            if any(pattern in user_input.lower() for pattern in data["patterns"]):
                response = random.choice(data["responses"])
                
                # Personalize response if we know the user's name
                if self.user_name:
                    response = response.replace("!", f", {self.user_name}!")
                
                return response
        
        # Handle sentiment-based responses
        if sentiment == "negative":
            return "I sense that you might be frustrated. How can I better assist you?"
        
        # Handle entities if found
        if any(entities.values()):
            return "I notice you've shared some specific information. Let me help you with that."
        
        # Check conversation history for context
        if len(self.conversation_history) > 1:
            prev_exchange = self.conversation_history[-2]
            if prev_exchange['sentiment'] == sentiment:
                return "I notice a pattern in our conversation. Let's explore this further."
        
        # Default response based on complexity of input
        if len(tokens) < 3:
            return "Could you provide more details about what you're looking for?"
        else:
            return "I understand you're asking about " + " ".join(tokens[:3]) + ". Could you clarify your specific needs?"

    def chat(self):
        """Main chat loop"""
        print("Bot: Hello! I'm your advanced AI assistant. Type 'quit' to exit.")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                if self.user_name:
                    print(f"Bot: Goodbye, {self.user_name}! Have a great day!")
                else:
                    print("Bot: Goodbye! Have a great day!")
                break
            
            response = self.generate_response(user_input)
            print("Bot:", response)

def main():
    # Initialize and start the chatbot
    chatbot = AdvancedChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main()