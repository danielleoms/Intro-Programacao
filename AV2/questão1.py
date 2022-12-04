#1- Senhas Criticadas- Faça um programa em Python que leia uma senha aleatória forneça seu tamanho, e imprima uma versão maiúscula e uma minúscula da senha.

password = input("Digite uma senha: ")
lenght = len(password)
passwordupper = password.upper()
passwordlower = password.lower()
start = password[0].isdigit()
contador = 0
cont = 0

for x in range (0, len(password)):
    number = password[x].isdigit()
    if number == True:
        contador = contador + 1

for x in range(0, len(password)):
    dupper = password[x].isupper()
    if dupper == True:
        cont = cont + 1
#(opcional) – incremente o programa e valide uma senha segundo os seguintes critérios:

if contador == 0:
    print("Senha inválida")

elif start == True:
    print("Senha inválida")

elif cont == 0:
    print("Senha inválida")

elif lenght < 6 or lenght > 8:
    print("Senha inválida")

else:
    print("Senha válida")
    print("Número de caracteres:",lenght)
    print("Saída em maiúsculo:",passwordupper)
    print("Saíde em minúsculo",passwordlower)
    print("Sua senha:",password)
