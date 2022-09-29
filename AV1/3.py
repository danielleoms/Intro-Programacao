#3.	Faça um programa em Python que leia um número inteiro N menor que 1.000
# e apresente todos os números ímpares de 1 a N, inclusive N


while n <= 1000:
    n = int(input('Insira um número'))
    if n % 2 != 0:
        print(n)