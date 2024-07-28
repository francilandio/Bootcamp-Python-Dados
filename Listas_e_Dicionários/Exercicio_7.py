# Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [22, 15, 30, 17, 18]
idades_igual_maior_18 = [idade for idade in idades if idade >= 18]

print(sorted(idades_igual_maior_18))