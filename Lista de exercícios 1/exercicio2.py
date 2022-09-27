# 2.	Escreva um programa que imprima os 100 primeiros números ímpares.
cont = -1
qtde = 0
for i in range(1,101):
    cont = cont + 2
    qtde = qtde + 1 #quantidade que o laço funciona
    print(cont, end=' ')
print('\nEsses são os {} primeiros números ímpares.'.format(qtde))
