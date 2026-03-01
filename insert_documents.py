# Nome: Leonardo Capistrano de Sousa Silva
from MongoBooks.connect_mongo import ConnectMongo
from MongoBooks.mongo_books_db import MongoBooksDB
from data.seed_data import author_data, category_data, get_initial_books, get_initial_orders

from constants import (
    BOLD_BLACK, BOLD_BLUE, BOLD_CYAN, BOLD_GREEN, BOLD_MAGENTA, 
    BOLD_RED, BOLD_WHITE, BOLD_YELLOW, RESET,
    COLLECTION_BOOKS, COLLECTION_AUTHORS, COLLECTION_CATEGORIES, COLLECTION_ORDERS
)

print(f"\n{BOLD_BLUE}Inserting data into collections{RESET}")

# Instanciando o conector e o gerenciador do banco de dados -----------------------------------------------------------
connector = ConnectMongo()
mongo_db = MongoBooksDB(connector)

# creating collections ----------------------------------------------------------------------------------------------------
books_col, authors_col, categories_col, orders_col = mongo_db.create_collections()

print(f"\n{BOLD_YELLOW}Collections created:{RESET}\n")
print("Books:", books_col)
print("Authors:", authors_col)
print("Categories:", categories_col)
print("Orders:", orders_col)

# inserting author data -------------------------------------------------------------------------------------------
print('\n')
mongo_db.insert_many_documents(COLLECTION_AUTHORS, author_data)

# inserting category data ----------------------------------------------------------------------------------------
mongo_db.insert_many_documents(COLLECTION_CATEGORIES, category_data)

# Get author and category IDs --------------------------------------------------------------------------------------
author_ids = {
    "Gabriel García Márquez": mongo_db.get_id(COLLECTION_AUTHORS, "name", "Gabriel García Márquez"),
    "William Shakespeare": mongo_db.get_id(COLLECTION_AUTHORS, "name", "William Shakespeare"),
    "Agatha Christie": mongo_db.get_id(COLLECTION_AUTHORS, "name", "Agatha Christie"),
    "Leo Tolstói": mongo_db.get_id(COLLECTION_AUTHORS, "name", "Leo Tolstói")
}

category_ids = {
    "Realismo Mágico": mongo_db.get_id(COLLECTION_CATEGORIES, "name", "Realismo Mágico"),
    "Teatro Clássico": mongo_db.get_id(COLLECTION_CATEGORIES, "name", "Teatro Clássico"),
    "Mistério e Policial": mongo_db.get_id(COLLECTION_CATEGORIES, "name", "Mistério e Policial"),
    "Romance Épico": mongo_db.get_id(COLLECTION_CATEGORIES, "name", "Romance Épico")
}

# book data ----------------------------------------------------------------------------------------------------
print(f"\n{BOLD_RED}Data in embedding{RESET}")
books_data = get_initial_books(author_ids, category_ids)

# inserting book data -------------------------------------------------------------------------------------------
mongo_db.insert_many_documents(COLLECTION_BOOKS, books_data)

# order data ---------------------------------------------------------------------------------------------------
print(f"\n{BOLD_RED}Data in linking{RESET}")
book_ids = {
    "Cem Anos de Solidão": mongo_db.get_id(COLLECTION_BOOKS, "title", "Cem Anos de Solidão"),
    "Romeu e Julieta": mongo_db.get_id(COLLECTION_BOOKS, "title", "Romeu e Julieta"),
    "Assassinato no Expresso do Oriente": mongo_db.get_id(COLLECTION_BOOKS, "title", "Assassinato no Expresso do Oriente"),
    "Guerra e Paz": mongo_db.get_id(COLLECTION_BOOKS, "title", "Guerra e Paz")
}

orders_data = get_initial_orders(book_ids)

# inserting order data ------------------------------------------------------------------------------------------
mongo_db.insert_many_documents(COLLECTION_ORDERS, orders_data)