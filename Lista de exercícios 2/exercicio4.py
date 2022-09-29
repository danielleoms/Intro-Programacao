#4.	Uma agência de uma cidade do interior tem, no máximo, 10.000 clientes. Faça um programa que leia o número da conta e o saldo de cada cliente. 
#A leitura de clientes termina quando for digitado -999 para número da conta ou quando atingir 10.000 clientes. 
#O programa deve calcular e imprimir o total de clientes com saldo negativo, o total de clientes da agência e o saldo da agência.

neg = 0
saldo_agência = 0
clientes = 0

resp = str(input("Você deseja começar a inserir os dados de clientes da agência: (S - Sim "
                 "e -999 para Sair): ")).strip().upper()

while resp != "-999" and clientes < 10000:
    print(f"\nCliente {clientes + 1}")
    conta = str(input("Insira a conta do cliente: "))
    saldo = float(input("Insira o saldo do cliente: "))
    if saldo < 0:
        neg += 1
    saldo_agência = saldo_agência + saldo
    print(saldo_agência)
    clientes += 1
    resp = str(input("\nVocê deseja inserir os dados de mais um cliente da agência: (S - Sim "
                     "e -999 para Sair):"))

print(f"Essa agência possui {clientes} clientes, {neg} clientes possuem saldo negativo e o saldo da agência é "
      f"{saldo_agência}.")
