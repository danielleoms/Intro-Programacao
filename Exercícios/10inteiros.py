#Escrever um programa que lê 10 valores inteiros para a variável “a”,
# #um de cada vez, e conta quantos destes valores são negativos,
# exibindo esta informação na tela.

for cont in range (0,11):
    print('\n A tabuada de {}' .format(cont))
    for x in range (0,11):
        print('{} * {} = {}' .format(cont,x,cont*x))
