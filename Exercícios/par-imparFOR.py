#Faça um programa que faça a leitura de 10 valores inteiros e, para cada valor,
# o programa deve informar se o número é par ou ímpar.
#for cont in range (para cada contagem limite)

for cont in range (1,11):
    num = int(input('Informe um número inteiro:'))
    rest = num % 2
    if rest == 0:
        print('O número {} é par'.format(num))
    else:
        print('O número {} é ímpar' .format(num))
