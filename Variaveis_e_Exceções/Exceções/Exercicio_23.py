# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o primeiro número: "))
    operador = (input("Digite o operador (+, -, *, /): "))

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
