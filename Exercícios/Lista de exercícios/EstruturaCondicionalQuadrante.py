# Faça um programa em Python que leia 2 valores com 1 casa decimal (x,y) que devem representar as coordenadas de um ponto em um plano.
# A seguir determine qual quadrante o ponto pertence, ou se está sobre algum dos eixos ou na origem (0,0)

x = float(input('X:'))
y = float(input('Y:'))

if x == 0 and y ==0:
    print('Origem')

elif x >= 1 and y >= 1:
        print('Quadrante 1')

elif x <= 1 and y >= 1:
        print('Quadrante 2')

elif x <= 1 and y <= 1:
        print('Quadrante 3')

elif x >= 1 and y <= 1:
        print('Quadrante 4')

else:
    if x == 0:
        print('Eixo X')
    if y == 0:
        print('Eixo Y')


#perguntar sobre como resolver a questão dos eixos
