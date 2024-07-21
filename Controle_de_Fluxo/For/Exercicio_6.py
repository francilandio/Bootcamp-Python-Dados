# Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "a raposa marrom salta sobre o cachorro preguiçoso, e o cachorro preguiçoso, corre atrás da raposa marrom."
texto_sem_pontos_virgulas = texto.replace(",", "").replace(".","")
palavras = texto_sem_pontos_virgulas.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)