#7. Faça um programa em Python que leia um número inteiro N menor que 10.000
#e apresente todos os números de 1 a N que divididos por N dão resto 2
# (Dica: use uma lógica similar àquele problema apresentar os números pares).


n = int(input('Digite um número inteiro menor que 10000:'))
cont=1

if n > 10000:
    print('Por favor, insira um número menor que 10000.')
else:
    while cont <= 10000:
        resto = cont % n
        if resto == 2:
            print(cont, end= ' ')
        cont += 1
