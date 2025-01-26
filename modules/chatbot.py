from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import json

chatbot = ChatBot(
    'Kc0',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'  # Database for storing data
)

with open('dataset.json', 'r') as f:
    data = json.load(f)

trainer = ListTrainer(chatbot)

for pair in data:
    trainer.train(pair)

def gen_response(msg: str):
    response = chatbot.get_response(msg)
    return response
