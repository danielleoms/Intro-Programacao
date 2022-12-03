soma = 0
jogo = list()

print('Digite 9 números inteiros para formar o de jogo da velha esquisito:\n')
for c in range(1, 3 + 1):
    linha = list()
    for i in range(1, 3 + 1):
        while True:
            try:
                valor = int(input(f'Digite o {i}º elemento da {c}ª linha: '))
                break
            except ValueError:
                print('Por favor, digite apenas valores inteiros!')
        if c == i:
            soma += valor
        linha.append(valor)
    jogo.append(linha)

print('-=-' * 10)

for x in jogo:
    for y in x:
        print(y, end='  ')
    print()
print('-=-' * 10)
print(f'A soma da diagonal principal é: {soma}')
