#3.	Vetores estranhos – criei um programa que solicite até 20 números inteiros positivos,
#e os armazene em um vetor. A entrada dos números termina ao chegar a 20 ou se o usuário digitar um valor negativo.
#Ao termina a entrada de dados imprima os números, a soma dos números, a quantidade entrada e a média. 


import statistics
lista = []

while len(lista)+1 <= 20:
    num = (int(input("Digite um número inteiro:")))
    if num <= 0:
     break
    else:
        lista.append(num)
     
print("Vetor:{}" .format(lista))
print("Quantidade de entrada:", len(lista))
print ("Soma:", sum(lista))
print("Média:", statistics.mean(lista))

#(opcional) – incremente o programa imprimindo também o maior e menor valor entrado

print('-=-' * 10)
print('         OPCIONAL')
print('-=-' * 10)

lista = []

while len(lista)+1 <= 20:
    num = (int(input("Digite um número inteiro:")))
    if num <= 0:
     break
    else:
        lista.append(num)
     
print("Vetor:{}" .format(lista))
print("Quantidade de entrada:", len(lista))
print ("Soma:", sum(lista))
print("Média:", statistics.mean(lista))
print ("O maior valor é:", max(lista))
print ("O menor valor é:", min(lista))
