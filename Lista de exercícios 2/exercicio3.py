#5.	Elabore um programa que calcule e imprima o valor de xn.
# O valor de n deverá ser maior do que 1 e inteiro e o valor de x deverá ser maior ou igual a 2 e inteiro.
# O cálculo da potência deve ser feito sem o uso de funções da biblioteca de math.

x = int(input('Informe um número inteiro para x:'))
n = int(input('Informe um número inteiro para n:'))

if n > 1 and x >= 2:
    print('O valor de {} elevado a {} é: {}.' .format(x, n, x ** n))
else:
    print('Por favor, insira novos valores.')
