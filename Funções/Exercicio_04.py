from typing import List

def celsius_para_fahrenheit(temperatura_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]


temperaturas_celsius = [0, 10, 20, 30, 40]
temperaturas_fahrenheit = celsius_para_fahrenheit(temperaturas_celsius)
print(temperaturas_fahrenheit)