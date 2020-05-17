"""
A Chatbot is a program simulates a conversation between a user and a computer

ChatterBot
- python library
- automated responses
- machine learning algorithms
- language independent
- train data
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
print(chatbot.get_response("what is AI?"))