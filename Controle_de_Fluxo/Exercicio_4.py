# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Insira uma idade: "))

if 18 <= idade <= 65:
    email = input("Insira um endereço de e-mail: ")
    if "@" not in email or "." not in email:
        print("E-mail inválido!")
    else:
        print("Dados de usuário, válidos.")
else:
    print("Idade fora do intervalo permitido.")