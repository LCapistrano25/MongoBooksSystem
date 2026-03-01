from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    """
    Interface abstrata para operações de banco de dados.
    """
    def __init__(self):
        self.client = None
        self.db = None
        
    @abstractmethod
    def connect(self):
        pass
