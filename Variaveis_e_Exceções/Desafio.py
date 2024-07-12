# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

CONSTANTE_BONUS = 1000

nome = input("Digite o seu nome: ")

if nome.isdigit():
    print("Digite um nome válido")
elif nome.isspace():
    print("Digite um nome válido")
elif len(nome) == 0:
    print("Digite um nome válido")
else:
    print(f"Olá, {nome}!")

try:
    salario = float(input("Qual o seu salário: "))
except ValueError:
    print("Digite um valor válido")

try:
    percentual_bonus = float(input("Qual o percentual de bônus? "))
except ValueError:
    print("Digite um valor válido")

# Cálculo do KPI do bônus de 2024 é de 1.000 + salário * bônus

resultado = CONSTANTE_BONUS + salario * percentual_bonus

print(f"Olá {nome}, o seu bônus é de {resultado}")