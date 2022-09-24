# Elabore um programa em Python que leia a medida de um raio de um círculo e efetue o cálculo da sua área, exibindo o resultado ao final. (dica: use math.pi )
#A área de um círculo é pi vezes o raio elevado ao quadrado (A = π r²).

import math
r = float(input('Informe o raio do círculo:'))
área = math.pi * (r ** 2)

print('A aréa é de {}' .format(área))
