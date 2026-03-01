import sys
import os
# Adicionando o diretório pai ao sys.path para importar 'constants'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pymongo import MongoClient, errors
from interface.connect_interface import DatabaseInterface
from constants import MONGO_URI, DB_NAME

class ConnectMongo(DatabaseInterface):
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(MONGO_URI)
            self.db = self.client[DB_NAME]
            print("\nConnected to database:", self.db)    
            return self.db
        except errors.ConnectionError as e:
            print("\nConnection error:", e)
        except Exception as e:
            print("\nAnother error occurred:", e)