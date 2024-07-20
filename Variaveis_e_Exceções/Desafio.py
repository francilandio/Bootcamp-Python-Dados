# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

CONSTANTE_BONUS = 1000

try:
    nome = input("Digite o seu nome: ")

    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print(f"Nome válido: {nome}")
except ValueError as e:
    print(e)

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
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para salário. Por favor, digite um número.")

try:
    percentual_bonus = float(input("Qual o percentual de bônus? "))
    if percentual_bonus < 0:
        print("Por favor, digite um valor positivo.")
except ValueError:
    print("Entrada inválida para salário. Por favor, digite um número.")

# Cálculo do KPI do bônus de 2024 é de 1.000 + salário * bônus

resultado = CONSTANTE_BONUS + salario * percentual_bonus

print(f"Olá {nome}, o seu bônus é de {resultado}")