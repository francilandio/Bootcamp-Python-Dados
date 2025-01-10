from typing import List

def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))

valores = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unicos = contar_valores_unicos(valores)
print(f"Existem {unicos} valores únicos na lista.")