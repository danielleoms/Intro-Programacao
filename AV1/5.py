#5. Faça um programa em Python que leia um número inteiro “N”, calcule e apresente todos os seus divisores.
#(Dica: use uma estrutura while para testar todos os possíveis divisores)


number = int(input('Insira um número: '))
c = 1
print(f'os divisores de {number} são: ')
while c <= number:
    resto  = number % c
    if resto == 0:
        print(c)
    c += 1
