# Faça um programa em Python que leia 1 valor de ponto flutuante
# e diga qual dos seguintes intervalos ele pertence: ([0,25], (25,50], (50,75], (75,100])
# Obs:
# [a,b] significa intervalo >= a e <=b
# (a,b] significa intervalo > a e <=b

num = float(input('Informe um número:'))

if num >= 0 and num <=25:
    print('Intervalo [0,25]')

elif num > 25 and num <=50:
    print('Intervalo (25,50]')

elif num > 50 and num <= 75:
    print('Intervalo (50,75]')

elif num > 75 and num <= 100:
    print('Intervalo (75,100]')

else:
  print('Fora de intervalo')
