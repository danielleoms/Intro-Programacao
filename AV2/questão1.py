#1.	Senhas Criticadas- Faça um programa em Python que leia uma senha
#aleatória e forneça seu tamanho, e imprima uma versão maiúscula e
#uma minúscula da senha. 

import random, string

print('Bem-vindo ao gerador de senhas!')
senha_length = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits 

password = ""   

for index in range(senha_length):
    password = password + random.choice(caracteres)

print("Senha gerada: {}".format(password))
print("Tamanho da senha:{}" .format(len(password)))
print("Versão maiúscula da senha: {}".format(password.upper()))
print("Versão minúscula da senha: {}".format(password.lower()))
