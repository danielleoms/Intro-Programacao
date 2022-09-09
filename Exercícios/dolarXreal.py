#Faça um programa em Python que leia um valor em dólar e efetue a apresentação do valor convertido em real
#O programa deve solicitar ao usuário o valor da cotação do dólar
#e a quantidade de dólares disponível, para que seja apresentado o valor em moeda brasileira.

cotdol= float(input('Valor da cotação do dólar hoje em relação ao real:'))
dolar = float(input('Quantos dólares ($) você tem na carteira?'))
real = cotdol * dolar

print('Com ${}, você tem R${}.'.format(dolar,real))
