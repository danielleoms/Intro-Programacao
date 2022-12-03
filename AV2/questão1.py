#1.	Senhas Criticadas- Faça um programa em Python que leia uma senha
#aleatória e forneça seu tamanho, e imprima uma versão maiúscula e
#uma minúscula da senha. 

password= str(input("Digite o tamanho da senha: "))


print("Senha gerada: {}".format(password))
print("Tamanho da senha:{}" .format(len(password)))
print("Versão maiúscula da senha: {}".format(password.upper()))
print("Versão minúscula da senha: {}".format(password.lower()))
