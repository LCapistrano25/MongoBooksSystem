# Nome: Leonardo Capistrano de Sousa Silva
from MongoBooks.connect_mongo import ConnectMongo
from MongoBooks.mongo_books_db import MongoBooksDB
from constants import (
    BOLD_BLUE, 
    BOLD_GREEN, 
    RESET,
    COLLECTION_BOOKS, 
    COLLECTION_AUTHORS, 
    COLLECTION_CATEGORIES, 
    COLLECTION_ORDERS
)
from data.operations_data import get_orwell_data, get_sample_order

# Instanciando o conector e o gerenciador do banco de dados -----------------------------------------------------------
connector = ConnectMongo()
mongo_db = MongoBooksDB(connector)

# fetching collections ----------------------------------------------------------------------------------------------------
books_col, authors_col, categories_col, orders_col = mongo_db.create_collections()

# inserting author data -------------------------------------------------------------------------------------------
print(f"\n{BOLD_BLUE}Inserting data into collections{RESET}")

# Preparamos os dados de Orwell (sem IDs ainda)
author_orwell = {
    "name": "George Orwell",
    "origin_country": "Reino Unido",
    "biography": "Autor de clássicos como '1984' e 'A Revolução dos Bichos', conhecido por suas críticas ao totalitarismo e às injustiças sociais."
}
mongo_db.insert_document(COLLECTION_AUTHORS, author_orwell)

print("\n")
# inserting category data -------------------------------------------------------------------------------------------
orwell_categories = [
    {"name": "Distopia", "description": "Obras que retratam sociedades opressivas e autoritárias."},
    {"name": "Fábula Política", "description": "Histórias simbólicas que satirizam sistemas políticos."},
]
mongo_db.insert_many_documents(COLLECTION_CATEGORIES, orwell_categories)

# inserting book data -------------------------------------------------------------------------------------------
print(f"{BOLD_GREEN}Get author and category IDs{RESET}\n")
orwell_author_id = mongo_db.get_id(COLLECTION_AUTHORS, "name", "George Orwell")
cat_ids = {
    "Distopia": mongo_db.get_id(COLLECTION_CATEGORIES, "name", "Distopia"),
    "Fábula Política": mongo_db.get_id(COLLECTION_CATEGORIES, "name", "Fábula Política")
}

_, _, orwell_books = get_orwell_data(orwell_author_id, cat_ids)

print("\n")
mongo_db.insert_many_documents(COLLECTION_BOOKS, orwell_books)

# inserting order data -------------------------------------------------------------------------------------------
print(f"{BOLD_GREEN}Get order IDs{RESET}\n")
book_ids = {
    "1984": mongo_db.get_id(COLLECTION_BOOKS, "title", "1984"),
    "A Revolução dos Bichos": mongo_db.get_id(COLLECTION_BOOKS, "title", "A Revolução dos Bichos")
}

order_data = get_sample_order(book_ids)

print("\n")
mongo_db.insert_many_documents(COLLECTION_ORDERS, order_data)

# updating author data -------------------------------------------------------------------------------------------
print(f"{BOLD_BLUE}Updating data in collections{RESET}\n")
mongo_db.update_document(COLLECTION_AUTHORS, "name", "George Orwell", {"biography": "Autor de clássicos como '1984' e 'A Revolução dos Bichos', conhecido por suas críticas ao totalitarismo e às injustiças sociais. Seu verdadeiro nome é Eric Arthur Blair."})

# showing all books -------------------------------------------------------------------------------------------
all_books_cursor = books_col.find()
mongo_db.find_all_books(all_books_cursor)

# deleting category -------------------------------------------------------------------------------------------------
mongo_db.delete_document(COLLECTION_CATEGORIES, "name", "Realismo Mágico")

# deleting book -----------------------------------------------------------------------------------------------------
mongo_db.delete_document(COLLECTION_BOOKS, "title", "Cem Anos de Solidão")

# querying books of a specific category ----------------------------------------------------------------------
print(f'\n{BOLD_GREEN}Get ID for "Teatro Clássico" category{RESET}')
classic_theater_category_id = mongo_db.get_id(COLLECTION_CATEGORIES, "name", "Teatro Clássico")

print(f"\n{BOLD_BLUE}Querying books from a specific category{RESET}")
mongo_db.query_document(COLLECTION_BOOKS, "category_ids", classic_theater_category_id)

# querying all orders from a specific customer -------------------------------------------------------------------------
print(f"{BOLD_BLUE}Querying orders from a specific customer{RESET}\n")
mongo_db.query_document(COLLECTION_ORDERS, "customer_name", "José Pereira")

# query books published by a specific author -------------------------------------------------------------
print(f"{BOLD_GREEN}Get ID for author 'George Orwell'{RESET}\n")
orwell_author_id = mongo_db.get_id(COLLECTION_AUTHORS, "name", "George Orwell")

print(f"\n{BOLD_BLUE}Querying books from a specific author{RESET}\n")
mongo_db.query_document(COLLECTION_BOOKS, "author_ids", orwell_author_id)

# filtering orders with "pendente" status ------------------------------------------------------------------------------
print(f"{BOLD_BLUE}Filtering orders with 'pendente' status{RESET}\n")
mongo_db.query_document(COLLECTION_ORDERS, "status", "pendente")