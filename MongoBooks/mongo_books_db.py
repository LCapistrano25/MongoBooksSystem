import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interface.connect_interface import DatabaseInterface
from constants import (
    BOLD_BLUE,
    BOLD_MAGENTA, 
    BOLD_RED, 
    BOLD_YELLOW, 
    RESET,
    COLLECTION_BOOKS, 
    COLLECTION_AUTHORS, 
    COLLECTION_CATEGORIES, 
    COLLECTION_ORDERS
)

class MongoBooksDB:
    def __init__(self, connect : DatabaseInterface):
        self.connect_mongo = connect
        self.db = self.connect_mongo.connect()

    # Método para criar coleções no banco de dados ------------------------------------------------------------------------
    def create_collections(self):
        return (self.db.get_collection(COLLECTION_BOOKS), 
                self.db.get_collection(COLLECTION_AUTHORS), 
                self.db.get_collection(COLLECTION_CATEGORIES), 
                self.db.get_collection(COLLECTION_ORDERS))

    def insert_many_documents(self, collection_name, data):
        """
        Insere vários documentos em uma coleção do banco de dados.

        :param collection_name: Nome da coleção onde os documentos serão inseridos.
        :param data: Lista de dicionários, onde cada dicionário representa um documento a ser inserido.
        """
        collection = self.db[collection_name]
        collection.insert_many(data)
        
        print(f"{BOLD_YELLOW}Documents inserted in collection '{collection_name}':{RESET}\n")
        for item in data:
            for key, value in item.items():
                print(f"{key}: {value}")
            print("\n")

    # Método para obter o ID de um documento no banco de dados -----------------------------------------------------------
    def get_id(self, collection_name, field, value):
        """
        Obtém o ID de um documento em uma coleção do banco de dados com base em um campo específico.

        :param collection_name: Nome da coleção onde o documento será buscado.
        :param field: Nome do campo a ser verificado (por exemplo, 'title', 'author', etc.).
        :param value: Valor do campo a ser comparado (por exemplo, 'J.K. Rowling', '2023', etc.).
        :return: O ID do documento se encontrado, ou None se nenhum documento for encontrado.
        """
        collection = self.db[collection_name]
        document = collection.find_one({field: value})
        
        if document:
            doc_id = document["_id"]
            print(f"Document ID with '{field}' equal to '{value}': {BOLD_MAGENTA}{doc_id}{RESET}", )
            return doc_id
        else:
            print("\nNo document found with '{}' equal to '{}'.".format(field, value))
            return None

    def insert_document(self, collection_name, data_item):
        """
        Insere um único documento em uma coleção do banco de dados.

        :param collection_name: Nome da coleção onde o documento será inserido.
        :param data_item: Dicionário representando o documento a ser inserido.
        """
        collection = self.db[collection_name]
        collection.insert_one(data_item)
        
        print(f"\n{BOLD_YELLOW}Document inserted in collection '{collection_name}':{RESET}\n")
        for key, value in data_item.items():
            print(f"{key}: {value}")

    def update_document(self, collection_name, field, value, new_value):
        """
        Atualiza um documento em uma coleção do banco de dados com base em um campo específico.

        :param collection_name: Nome da coleção onde o documento será atualizado.
        :param field: Nome do campo a ser verificado (por exemplo, 'title', 'author', etc.).
        :param value: Valor do campo a ser comparado (por exemplo, 'J.K. Rowling', '2023', etc.).
        :param new_value: Novo valor a ser definido para o campo especificado.
        """
        collection = self.db[collection_name]
        collection.update_one({field: value}, {"$set": new_value})
        updated_document = collection.find_one({field: value})
        print(f"{BOLD_YELLOW}Document updated in collection '{collection_name}':{RESET}\n")
        for key, doc in updated_document.items():
            print(f"{key}: {doc}")

    def find_all_books(self, books_cursor):
        """
        Exibe todos os livros em uma coleção do banco de dados.

        :param books_cursor: Cursor contendo os documentos dos livros.
        """
        print(f"\n{BOLD_BLUE}All books in collection 'books':{RESET}\n")
        for book in books_cursor:
            print(f"Title: {book['title']}")
            print(f"Publication Year: {book['publication_year']}")
            print(f"Price: R$ {book['price']:.2f}")

            # Exibir autores relacionados
            author_ids = book.get("author_ids", [])
            author_names = [self.db.authors.find_one({"_id": author_id})["name"] for author_id in author_ids]
            print(f"Authors: {', '.join(author_names)}")

            # Exibir categorias relacionadas
            category_ids = book.get("category_ids", [])
            category_names = [self.db.categories.find_one({"_id": category_id})["name"] for category_id in category_ids]
            print(f"Categories: {', '.join(category_names)}")
            print("-" * 40)  # Separador entre livros

    def delete_document(self, collection_name, field, value):
        """
        Deleta um documento em uma coleção do banco de dados com base em um campo específico.

        :param collection_name: Nome da coleção onde o documento será deletado.
        :param field: Nome do campo a ser verificado (por exemplo, 'title', 'author', etc.).
        :param value: Valor do campo a ser comparado (por exemplo, 'J.K. Rowling', '2023', etc.).
        """
        collection = self.db[collection_name]
        collection.delete_one({field: value})
        print(f"{BOLD_RED}\nDocument deleted from collection '{collection_name}':{RESET}")
        print(f"{field}: {value}")
        print(f"{collection}")

    def query_document(self, collection_name, field, value):
        """
        Consulta um documento em uma coleção do banco de dados com base em um campo específico.

        :param collection_name: Nome da coleção onde o documento será consultado.
        :param field: Nome do campo a ser verificado (por exemplo, 'title', 'author', etc.).
        :param value: Valor do campo a ser comparado (por exemplo, 'J.K. Rowling', '2023', etc.).
        :return: O documento encontrado se existir, ou None se nenhum documento for encontrado.
        """
        collection = self.db[collection_name]
        document = collection.find_one({field: value})
        if document:
            print(f"{BOLD_YELLOW}Document found in collection '{collection_name}':{RESET}\n")
            for key, val in document.items():
                print(f"{key}: {val}")
            print("\n")
            return document
        else:
            print(f"\nNo document found in '{collection_name}' with '{field}' equal to '{value}'.")
            return None
