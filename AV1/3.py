#3.	Faça um programa em Python que leia um número inteiro N menor que 1.000 e apresente todos os números ímpares de 1 a N,
# inclusive N

# Usando for

n = int(input('Informe um número menor que 1000:'))
if n > 1000:
    print('Informe um número menor que 1000.')
else:
    for c in range(1, n+1):
        if c % 2 != 0:
            print(c, end=' ')
