# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    num = int(input("Digite um número: "))
    if num > 0:
        print("Positivo")
    elif num < 0:
        print("Negativo")
    else:
        print("Zero")
    if num % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Digite um número válido.")