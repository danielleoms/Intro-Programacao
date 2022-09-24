"""Faça um programa em Python que leia 3 valores de ponto flutuante e efetue o cálculo das raízes usando a equação de Bhaskara.
 Se não for possível calcular as raízes, caso haja uma divisão por 0 ou uma raiz quadrada de número negativo,
 apresente a mensagem “impossível calcular a raiz”
 FÓRMULA DE BHASKARA: x = (-b ± √( b² - 4 a c ) ) / 2 a"""

import math
a = float(input('Entre com o valor de a:'))
b = float(input('Entre com o valor de b:'))
c = float(input('Entre com o valor de c:'))

delta  = ( b**2 )-(4 * a * c)

if a == 0 or delta < 0:
        print ("Impossível calcular.")

else :
    x=math.sqrt(delta)
    x1 = (-b+x)/(2*a)
    x2 = (-b-x)/(2*a)
    print('R1 = {:.4f} R2 = {:.4f}' .format(x1, x2))
