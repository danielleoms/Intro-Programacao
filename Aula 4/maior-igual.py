#Escreva um programa em Python que leia dois
# números inteiros e informe a relação entre eles: se são iguais,
# se o primeiro é maior do que o segundo ou se o segundo é maior do que o primeiro.

num1= int(input('Escreva um número inteiro:'))
num2= int(input('Escreva novamente um número inteiro:'))

if num1 == num2:
    print('Os números são iguais')
else:
    if num1 > num2:
        print('O número',num1, 'é maior que',num2)

    else:
        print('O', num2, 'é maior que o que', num1)
