# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista = ["maçã", "banana", "cereja"]
precos = {"maçã": 5.45, "banana": 3.30, "cereja": 10.65}

total = sum(precos[item] for item in lista)
print(f"Preço total: {total}")