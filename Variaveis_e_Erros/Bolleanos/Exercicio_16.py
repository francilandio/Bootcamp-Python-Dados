# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = bool(input("Insira o valor True ou False: "))
valor2 = bool(input("Insira o novamente o valor True ou False: "))

resultado_and = valor1 and valor2

print(f"O resultado dos dois valores comparados com AND é: {resultado_and}")