# Faça um programa que converta a temperatura de Celsius para Fahrenheit.

try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}ºF")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")