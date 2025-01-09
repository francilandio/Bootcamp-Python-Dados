from typing import List

def filtra_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
            print(f"O valor {valor} é maior que {limite}")
    return resultado

valores = [15, 22, 33, 40, 54]
acima_de_2 = filtra_acima_de(valores, 30)