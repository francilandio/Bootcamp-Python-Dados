# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero = int(input("Digite um número entre 1 e 5: "))

while numero < 1 or numero > 10:
    print("Número fora do intervalo.")
    numero = int(input("Digite um número entre 1 e 5: "))

print("Número válido!")