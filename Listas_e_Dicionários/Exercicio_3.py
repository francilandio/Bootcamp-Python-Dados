# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

info_livro = {
    "título": "Ultraaprendizado",
    "autor": "Fulano",
    "ano": "2020"
}

for chave, valor in info_livro.items():
    print(f"{chave.capitalize()}: {valor}")