#2.	Faça um programa que leia os 3 lados de um triangulo e determine se ele é um triangulo retângulo.
# Para isto utilize a fórmula do item anterior nesta checagem.

a = float(input('Digite o valor do primeiro segmento: '))
b = float(input('Digite o valor do segundo segmento: '))
c = float(input('Digite o valor do terceiro segmento: '))

if c == ((a **2) + (b **2)) **(1/2) or a == ((c **2) + (b **2)) **(1/2) or b == ((a **2) + (c **2)) **(1/2):
    print(f'Os lados {a},{b} e {c} formam um triângulo retângulo')

else:
    print(f'Os lados {a},{b} e {c} NÃO formam um triângulo retângulo')
