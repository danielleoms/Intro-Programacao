#Faça um programa para ler dois inteiros e imprimir o resultado do quadrado da diferença do primeiro valor pelo segundo.

num1 = int(input('Primeiro número:'))
num2 = int(input('Segundo número:'))
cal = (num1 - num2)**2
print('O resultado do quadrado da diferença de {} e {} é {}'.format(num1,num2,cal))
