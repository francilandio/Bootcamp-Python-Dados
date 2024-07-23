# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "parar", 14, 15, 16 ,17, 18]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada econtrada, encerrando o processamento.")
        break
    print(f"Processando próximo item: {itens[i]}")
    i += 1