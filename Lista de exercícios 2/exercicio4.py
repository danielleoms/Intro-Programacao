#4.	Uma agência de uma cidade do interior tem, no máximo, 10.000 clientes. Faça um programa que leia o número da conta e o saldo de cada cliente. 
#A leitura de clientes termina quando for digitado -999 para número da conta ou quando atingir 10.000 clientes. 
#O programa deve calcular e imprimir o total de clientes com saldo negativo, o total de clientes da agência e o saldo da agência.

n = int(input("Quantos números você quer que a sequência tenha? "))
S = 1
print("A sequência é", S, end="")
for cont in range(1, n):
    S += (2 * cont) + 1
    print(f", {S}", end="")
