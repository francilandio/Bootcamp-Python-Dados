from typing import List

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

valores = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 16, 18, 40]
valores_ausentes = encontrar_valores_ausentes(valores)
print(f"Os valores ausentes na sequência sao: {valores_ausentes}")