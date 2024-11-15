import random
import json
import time
from datetime import datetime

class AdvancedChatbot:
    def __init__(self):
        # Initialize the chatbot's knowledge base
        self.knowledge_base = {
            "greetings": [
                "Hello! How can I help you today?",
                "Hi there! What brings you here?",
                "Greetings! How may I assist you?"
            ],
            "farewells": [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! Hope to chat again soon!"
            ],
            "thanks": [
                "You're welcome!",
                "Glad I could help!",
                "My pleasure!"
            ],
            "unknown": [
                "I'm not sure I understand. Could you rephrase that?",
                "Could you explain that differently?",
                "I'm still learning. Can you elaborate?"
            ]
        }
        
        # Pattern matching dictionary
        self.patterns = {
            "greeting": ["hello", "hi", "hey", "morning", "evening", "afternoon"],
            "farewell": ["bye", "goodbye", "see you", "later", "exit", "quit"],
            "thanks": ["thank", "thanks", "appreciate"],
            "help": ["help", "assist", "support"],
            "time": ["time", "hour", "clock"],
            "name": ["your name", "who are you", "what are you"],
            "weather": ["weather", "temperature", "forecast"],
            "how_are_you": ["how are you", "how do you feel", "how're you"]
        }
        
        self.conversation_history = []
        self.user_name = None

    def get_current_time(self):
        """Return current time in a readable format"""
        return datetime.now().strftime("%I:%M %p")

    def identify_intent(self, message):
        """Identify the intent of the user's message"""
        message = message.lower()
        
        for intent, pattern_list in self.patterns.items():
            if any(pattern in message for pattern in pattern_list):
                return intent
        return "unknown"

    def remember_name(self, message):
        """Try to extract name from message"""
        message = message.lower()
        if "my name is" in message:
            self.user_name = message.split("my name is")[-1].strip().title()
            return True
        elif "i am" in message:
            self.user_name = message.split("i am")[-1].strip().title()
            return True
        return False

    def generate_response(self, message):
        """Generate an appropriate response based on the message"""
        # Check if user is sharing their name
        if self.remember_name(message):
            return f"Nice to meet you, {self.user_name}! How can I help you today?"
        
        # Identify the intent of the message
        intent = self.identify_intent(message)
        
        # Generate response based on intent
        if intent == "greeting":
            return random.choice(self.knowledge_base["greetings"])
        
        elif intent == "farewell":
            return random.choice(self.knowledge_base["farewells"])
        
        elif intent == "thanks":
            return random.choice(self.knowledge_base["thanks"])
        
        elif intent == "time":
            return f"The current time is {self.get_current_time()}"
        
        elif intent == "name":
            return "I'm ChatBot, an AI assistant designed to help you!"
        
        elif intent == "weather":
            return "I'm sorry, I don't have access to weather information. You might want to check a weather website or app."
        
        elif intent == "how_are_you":
            return "I'm functioning well, thank you! How can I assist you?"
        
        elif intent == "help":
            help_message = """
I can help you with several things:
1. Answer basic questions
2. Tell you the current time
3. Remember your name
4. Have a friendly conversation
What would you like to know more about?"""
            return help_message
        
        # If no specific intent is identified
        return random.choice(self.knowledge_base["unknown"])

    def chat(self):
        """Main chat loop"""
        print("ChatBot: Hello! I'm your AI assistant. Type 'quit' to exit.")
        
        while True:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit command
            if user_input.lower() in ['quit', 'exit', 'bye']:
                farewell = random.choice(self.knowledge_base["farewells"])
                if self.user_name:
                    print(f"ChatBot: Goodbye, {self.user_name}! {farewell}")
                else:
                    print(f"ChatBot: {farewell}")
                break
            
            # Generate and print response
            response = self.generate_response(user_input)
            print("ChatBot:", response)
            
            # Store conversation history
            self.conversation_history.append({
                "user": user_input,
                "bot": response,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

def main():
    chatbot = AdvancedChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main()