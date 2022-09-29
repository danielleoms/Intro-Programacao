#2.	Faça um programa que leia os 3 lados de um triangulo e determine se ele é um triangulo retângulo.
# Para isto utilize a fórmula do item anterior nesta checagem.

cateto1 = float(input('Digite o valor do primeiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto: '))
hi = float(input('Digite o valor da hipotenusa: '))
((cateto1 ** 2) + (cateto2 ** 2)) ** (1/2)

if hi == ((cateto1 ** 2) + (cateto2 ** 2)) ** (1/2):
    print(f'Os lados {cateto1},{cateto2} e {hi} formam um triângulo retângulo')

else:
    print(f'Os lados {cateto1},{cateto2} e {hi} não formam um triângulo retângulo')
