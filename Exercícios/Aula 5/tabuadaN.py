#Faça um programa que imprima a tabuada de um numero “n”
# (dado de entrada do seu programa) utilizando estrutura de repetição.

num = int(input('Informe um valor:'))
for cont in range (0,11):
    tab = cont * num
    print('{} * {} é {}' .format(num,cont,tab))
