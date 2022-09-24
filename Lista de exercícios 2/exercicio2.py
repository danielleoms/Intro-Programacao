#Escreva um programa que calcule o valor da hipotensa de um triangulo retângulo,
# dado o valor de cada um dos catetos.

#obs: fórmula do cálculo da hipotenusa: a² + b² = c²

cateto1 = float(input('Informe o valor do primeiro cateto:'))
cateto2 = float(input('Informe o valor do segundo cateto:'))
hi = ((cateto1 ** 2) + (cateto2 ** 2)) ** (1/2)

print('O valor da hipotenusa é {:.1f}' .format(hi))

# Utilizando import math

from math import sqrt

cateto1 = float(input('Informe o valor do primeiro cateto:'))
cateto2 = float(input('Informe o valor do segundo cateto:'))
hi = sqrt(cateto1 ** 2 + cateto2 ** 2)
print('O valor da hipotenusa é {:.1f}' .format(hi))
