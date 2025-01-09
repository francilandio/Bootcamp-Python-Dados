from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

valores = [1, 2, 3, 4, 5]
media = calcular_media(valores)
print(f"A média dos números é: {media}")