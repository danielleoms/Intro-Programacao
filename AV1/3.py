#3.	Faça um programa em Python que leia um número inteiro N menor que 1.000 e apresente todos os números ímpares de 1 a N,
# inclusive N

# Utilizando while

n = int(input("Digite um número menor que 1000:"))
x = 0
if n > 1000:
    print('Informe um número menor que 1000.')
else:
    while x <= n:
        if x % 2 != 0:
            print(x, end=' ')
        x = x + 1

# Usando for

n = int(input('\nInforme um número menor que 1000:'))
if n > 1000:
    print('Informe um número menor que 1000.')
else:
    for c in range(1, n+1):
        if c % 2 != 0:
            print(c, end=' ')
