# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. 
# Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura = int(input("Insira uma temperatura: "))

if temperatura < 18:
    print("A temperatura está: Baixa")
elif 18 <= temperatura <= 26:
    print("A temperatura está: Normal")
else:
    print("A temperatura está: Alta")