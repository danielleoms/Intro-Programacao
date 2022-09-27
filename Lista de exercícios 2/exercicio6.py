#6.	Escreva um programa que lê um valor n inteiro e positivo e que
# calcula a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n.

n = int(input('Informe um número:'))
soma = 0
calc = 0

if n < 0:
    print('Informe um número positivo.')
else:
    for c in range(1, n+1):
        calc = 1 / c
        soma += calc
    print(soma, end=' ')

#verificar se está correto
