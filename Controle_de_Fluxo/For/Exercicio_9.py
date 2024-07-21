# Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [num for num in numeros if num % 2 == 0]

print(pares)