# Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Carla", "idade": 20},
    {"nome": "Alice", "idade": 30},
    {"nome": "Carol", "idade": 20},
    {"nome": "Diego", "idade": 35},
    {"nome": "Bob", "idade": 25},
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30}
]

lista_ordenada_nome = sorted(pessoas, key=lambda x: x["nome"])

print(lista_ordenada_nome)