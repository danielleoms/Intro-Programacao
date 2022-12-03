#2.	Senhas Criticadas com funções – rescreva o programa do exercício anterior, criando e utilizando as seguintes funções:

def lenght (p, min, max):
  if min <= len(p) <= max:
    return True
  else:
    return False
  
  def passwordupper(p):
    return p.upper()
  
  def passwordlower(p):
    return p.lower()

#(opcional). Acrescente as seguintes funções:
def valid1dig(p):
    for i in p:
        if i.isnumeric():
            return True
    return False
    
def no1number(p):
    if p[0].isnumeric(): 
        return True
    else:
        return False
        
def pelomenos1maisc(p):
    for i in p:
        if i.isupper():
            return True
    return False
        
while True:
    password= str(input("Digite o tamanho da senha: "))
    if lenght(password, 6, 8 ) and valid1dig(password)  and no1number(password) and pelomenos1maisc(password):
        break 
    if not lenght(password, 6, 8 ):
        print("SENHA INVÁLIDA! Sua senha deve ter entre 6 e 8 caracteres.")
    if not no1number(password):
        print("SENHA INVÁLIDA! Sua senha precisa começar com um número.")
    if not pelomenos1maisc(password):
        print("SENHA INVÁLIDA! Sua senha precisa ter pelo menos uma letra maiúscula.")
print("Senha válida! Sua senha contém: {}" .format(len(password)))
print("Versão maiúscula da senha: {}".format(password.upper()))
print("Versão minúscula da senha: {}".format(password.lower()))
