#4.	Faça um programa em Python que leia um conjunto indeterminado de dados, contendo cada um a idade de um indivíduo, e calcule e imprima a média de idades do grupo.
# O último dado, que não entrará no cálculo da média deve ser um valor negativo.

x = 0
soma = 0
qntd = 0
while x >= 0:
    x = int(input('Informe a idade do indivíduo e para finalizar o programa digite um número negativo: '))
    if x >= 0:
        qntd += 1
        soma += x
media = soma / qntd
print('A média de idade do grupo de {} pessoas é {:.2f}'.format(qntd, media))
