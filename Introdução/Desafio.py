# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = input("Digite o seu nome: ")
salario = float(input("Qual o seu salário: "))
percentual_bonus = float(input("Qual o percentual de bônus? "))

# Cálculo do KPI do bônus de 2024 é de 1.000 + salário * bônus

resultado = 1000 + salario * percentual_bonus

print(f"Olá {nome}, o seu bônus é de {resultado}")