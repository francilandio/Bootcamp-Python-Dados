from typing import List

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

valores = [1, 2, 3, 4, 5]
desvio_padrao = calcular_desvio_padrao(valores)
print(f"O desvio padrão dos números é: {desvio_padrao}")