
#Escreva o menu de opções abaixo. Leia a opção do usuário,
# leia os numeros e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.


print('-=-' * 10 )
print('        CALCULADORA')
print('-=-' * 10 )

num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))

opcao = 0
while opcao != 5:
    print('-=-' * 10)
    print('''Escolha a opção desejada:
    [ 1 ] Soma de 2 números inteiros
    [ 2 ] Diferença entre 2 números 
    [ 3 ] Produto entre 2 números
    [ 4 ] Divisão entre 2 números 
    [ 5 ] Sair ''')
    opcao = int(input('Sua opção:'))
    if opcao == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        if num1 > num2:
            print(f'{num1} - {num2} = {num1 - num2}')
        if num1 < num2:
            print(f'{num2} - {num1} = {num2 - num1}')
    elif opcao == 3:
        print('{} X {} ='.format(num1, num2, num1 * num2))
    elif opcao == 4:
        if num1 == 0:
            print(f'{num1} ÷ {num2} = {num1 / num2}')
        if num2 == 0:
            print(f'{num2} ÷ {num1} = {num2 / num1}')
    elif opcao == 5:
        print('Fim do progama! Volte sempre.')
    else:
        print('Por favor, escolha uma opção válida.')
