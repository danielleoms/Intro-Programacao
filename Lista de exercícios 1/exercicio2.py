# 2.Escreva um programa que imprima os 100 primeiros números ímpares.

#fórmula do N-ésimo termo:
#N-ésimo = primeiroNumero + (ultimoNumero - 1) * razão

cont = 0
x = 1 + (100 - 1) * 2
for c in range(1, x + 2):
    if c % 2 != 0:
        print(c, end=' ')
        cont += 1
print('\nEsses são os {} primeiros números ímpares.'.format(cont))

