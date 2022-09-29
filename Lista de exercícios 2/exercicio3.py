# 3.	Faça um programa que leia a média de alunos de uma determinada turma, encontre e exiba o maior valor de média inserida.
# Obs.: Não há informação prévia sobre a quantidade de alunos da turma

resp = str(input("Você gostaria de informar as notas de um aluno da turma"
                 "(S para Sim e N para Não): ")).strip().upper()
maior_media = 0

while resp == "S":
    media = float(input("Insira a média de um aluno: "))
    if media > maior_media:
        maior_media = media
    resp = str(input("\nVocê gostaria de informar as notas de mais um aluno da turma"
                     "(S para Sim e N para Não): ")).strip().upper()

print(f"A maior média entre os alunos é {maior_media}.")

