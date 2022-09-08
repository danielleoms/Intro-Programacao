#media dos alunos
nota1= float(input("Informe a primeira nota:"))
nota2= float(input("Informe a segunda nota:"))
media = (nota1 + nota2)/2
print('A sua nota ? {}' .format(media))

if media >= 7.0:
    print('Parabens, voce esta aprovado')

else:
    print('Que pena, voce esta reprovado')
