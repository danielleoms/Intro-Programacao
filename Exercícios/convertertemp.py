#Faça um programa em Python que calcule a temperatura em graus Fahrenheit, dado como entrada a temperatura em graus Celsius 
#use a formula C/5=(F-32)/9  ou F=(9/5)*C+32 

c = float(input('Informe a temperatura em ºC: '))
f = 9/ 5 * c + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
