# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

lista_num = input("Digite uma lista de números separados por vírgula: ")
num_str = lista_num.split(",")
num_int = []

try:
    for num in num_str:
        num_int.append(int(num.strip()))
    print(f"Lista de inteiros: {num_int}")
except:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")