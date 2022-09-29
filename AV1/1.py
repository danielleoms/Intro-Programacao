#1.	Faça um programa que calcule e apresente o valor da hipotenusa “c” de um
# triângulo retângulo, dado o valor de seus catetos “a” e “b”, segundo a fórmula:

#fórmula do cálculo da hipotenusa: a² + b² = c²

cateto1 = float(input('Informe o valor do primeiro cateto:'))
cateto2 = float(input('Informe o valor do segundo cateto:'))
hi = ((cateto1 ** 2) + (cateto2 ** 2)) ** (1/2) #não esquecer de colocar o 1/2 entre parentêses

print('O valor da hipotenusa é {:.1f}' .format(hi))
