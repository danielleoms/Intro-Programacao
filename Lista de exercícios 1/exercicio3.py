#3.	Escreva um programa que imprima todos os números pares compreendidos entre 85 e 907. O programa deve também calcular a soma destes valores. 

#Verificando se é divisível por 2

print('Os números pares compreendidos entre 85 e 907 são:')
s=0
for n in range (85, 907):
    if n % 2 == 0:
        print(n)
        s += n
print('O somatório de todos os valores foi {}.'.format(s))
print('FIM')
