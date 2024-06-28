# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

valor1 = int(input("Insira um número inteiro: "))
valor2 = int(input("Insira novamente um número inteiro: "))

resultado_diferente = valor1 != valor2

print(f"O resutlado se os números são diferentes é: {resultado_diferente}")