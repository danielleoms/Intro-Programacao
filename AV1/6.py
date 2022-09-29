#6.	Um posto de combustível deseja gerenciar a preferência de produto por seus clientes.
# Para isto é solicitado um programa em Python que leia o código do combustível escolhido segundo a tabela abaixo:

#Caso o usuário digite um valor inválido, deve ser solicitado um novo valor até que seja válido. O programa é encerrado quando se digita o código 4,
# quando então o cálculo é feito e a mensagem “Muito Obrigado” juntamente com a resposta é apresentada.

contG = 0
contA = 0
contD = 0
opcao = 0
while opcao != 4:
    print('-=-' * 10)
    print('''Preferência de produto:
    [ 1 ] GASOLINA
    [ 2 ] ÁLCOOL
    [ 3 ] DIESEL
    [ 4 ] FIM ''')
    opcao = int(input('Sua opção:'))
    if opcao == 1:
        contG += 1
        print('Gasolina: 1')
    elif opcao == 2:
        contA += 1
        print('Álcool: 2')
    elif opcao == 3:
        contD += 1
        print('Diesel: 3')
    elif opcao == 4:
        print('FIM.')
    else:
        print('Por favor, escolha uma opção válida.')
print('Muito obrigada!')
print('''As preferências são:
      Gasolina:{}
      Álcool:{}
      Diesel:{}''' .format(contG, contA, contD))
