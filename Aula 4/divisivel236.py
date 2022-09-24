#Escreva um programa em Python que leia um número inteiro e
#informe se ele é divisível por 2, por 3 ou por 6 (divisível por 2 e 3).

num= int(input('Escreva um número inteiro:'))

if num % 6 == 0:
    print('O número {} é divisível por 6.'.format(num))

else:
    if num % 2 == 0:
        print('O número {} é divisível por 2'.format(num))

    if num % 3 == 0:
        print('O número {} é divisível por 3'.format(num))
