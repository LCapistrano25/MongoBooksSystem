def get_orwell_data(author_id, category_ids):
    """
    Retorna os dados relacionados a George Orwell.
    Expects category_ids dictionary with names as keys.
    """
    author = {
        "name": "George Orwell",
        "origin_country": "Reino Unido",
        "biography": "Autor de clássicos como '1984' e 'A Revolução dos Bichos', conhecido por suas críticas ao totalitarismo e às injustiças sociais."
    }

    categories = [
        {"name": "Distopia", "description": "Obras que retratam sociedades opressivas e autoritárias."},
        {"name": "Fábula Política", "description": "Histórias simbólicas que satirizam sistemas políticos."},
    ]

    books = [
        {
            "title": "1984",
            "publication_year": 1949,
            "price": 49.90,
            "author_ids": [author_id],
            "category_ids": [category_ids["Distopia"]]
        },
        {
            "title": "A Revolução dos Bichos",
            "publication_year": 1945,
            "price": 39.90,
            "author_ids": [author_id],
            "category_ids": [category_ids["Fábula Política"]]
        }
    ]

    return author, categories, books

def get_sample_order(book_ids):
    """
    Retorna pedidos de exemplo para operacoes.py.
    """
    return [
        {
            "customer_name": "Daniel Alves", 
            "items": [{"book_id": book_ids["1984"], "quantity": 1}], 
            "status": "pendente"
        },
        {
            "customer_name": "Neymar Junior",
            "items": [{"book_id": book_ids["A Revolução dos Bichos"], "quantity": 2}],
            "status": "concluído"
        }
    ]
