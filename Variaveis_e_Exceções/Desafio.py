# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

CONSTANTE_BONUS = 1000
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

# Loop de entrada e verificação do nome
while not nome_valido:
    try:
        nome: str = input("Digite o seu nome: ")

        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        elif nome.isspace():
            raise ValueError("Digite um nome válido.")
        else:
            print(f"Nome válido: {nome}")
            nome_valido: bool = True
    except ValueError as e:
        print(e)

# Loop para entrada e verificação de salário
while not salario_valido:
    try:
        salario: float = float(input("Qual o seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido: bool = True
    except ValueError:
        print("Entrada inválida para salário. Por favor, digite um número.")

# Loop para entrada e verificação de bônus
while not bonus_valido:
    try:
        bonus: float = float(input("Qual o percentual de bônus? "))
        if bonus < 0:
            print("Por favor, digite um valor positivo.")
        else:
            bonus_valido: bool = True
    except ValueError:
        print("Entrada inválida para salário. Por favor, digite um número.")

# Cálculo do KPI do bônus de 2024 é de 1.000 + salário * bônus

resultado: float = CONSTANTE_BONUS + salario * bonus

print(f"Olá {nome}, o seu bônus é de {resultado}")