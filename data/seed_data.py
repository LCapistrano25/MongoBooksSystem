# Dados de exemplo: Autor ---------------------------------------------------------------------------------------------
author_data = [
    {
        "name": "Gabriel García Márquez",
        "origin_country": "Colômbia",
        "biography": "Autor de 'Cem Anos de Solidão', vencedor do Prêmio Nobel de Literatura."
    },
    {
        "name": "William Shakespeare",
        "origin_country": "Reino Unido",
        "biography": "Autor de peças clássicas como 'Romeu e Julieta', conhecido como o maior dramaturgo da língua inglesa."
    },
    {
        "name": "Agatha Christie",
        "origin_country": "Reino Unido",
        "biography": "Autora de obras policiais como 'Assassinato no Expresso do Oriente', conhecida como a Rainha do Crime."
    },
    {
        "name": "Leo Tolstói",
        "origin_country": "Rússia",
        "biography": "Autor de 'Guerra e Paz' e 'Anna Karenina', obras-primas da literatura russa."
    }
]

# Dados de exemplo: Categorias -----------------------------------------------------------------------------------------
category_data = [
    {
        "name": "Realismo Mágico",
        "description": "Histórias que combinam elements mágicos e fantásticos com a realidade cotidiana."
    },
    {
        "name": "Teatro Clássico",
        "description": "Peças que exploram temas universais como amor, tragédia e poder, escritas durante o Renascimento."
    },
    {
        "name": "Mistério e Policial",
        "description": "Narrativas que envolvem investigação, crimes e enigmas a serem resolvidos."
    },
    {
        "name": "Romance Épico",
        "description": "Histórias grandiosas que exploram questões sociais e históricas profundas."
    }
]

def get_initial_books(author_ids, category_ids):
    """
    Retorna a lista de livros para inserção inicial.
    Expects author_ids and category_ids dictionaries with names as keys.
    """
    return [
        {
            "title": "Cem Anos de Solidão",
            "publication_year": 1967,
            "price": 59.90,
            "author_ids": [author_ids["Gabriel García Márquez"]],
            "category_ids": [category_ids["Realismo Mágico"]]
        },
        {
            "title": "Romeu e Julieta",
            "publication_year": 1597,
            "price": 39.90,
            "author_ids": [author_ids["William Shakespeare"]],
            "category_ids": [category_ids["Teatro Clássico"]]
        },
        {
            "title": "Assassinato no Expresso do Oriente",
            "publication_year": 1934,
            "price": 45.90,
            "author_ids": [author_ids["Agatha Christie"]],
            "category_ids": [category_ids["Mistério e Policial"]]
        },
        {
            "title": "Guerra e Paz",
            "publication_year": 1869,
            "price": 89.90,
            "author_ids": [author_ids["Leo Tolstói"]],
            "category_ids": [category_ids["Romance Épico"]]
        }
    ]

def get_initial_orders(book_ids):
    """
    Retorna a lista de pedidos iniciais.
    Expects book_ids dictionary with titles as keys.
    """
    return [
        {
            "customer_name": "José Pereira", 
            "items": [{"book_id": book_ids["Cem Anos de Solidão"], "quantity": 3}], 
            "status": "concluído"
        },
        {
            "customer_name": "Leonardo Silva", 
            "items": [
                {"book_id": book_ids["Romeu e Julieta"], "quantity": 1}, 
                {"book_id": book_ids["Guerra e Paz"], "quantity": 2}
            ], 
            "status": "em andamento"
        },
        {
            "customer_name": "João Souza", 
            "items": [{"book_id": book_ids["Assassinato no Expresso do Oriente"], "quantity": 2}], 
            "status": "cancelado"
        }
    ]
