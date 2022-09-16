# Calcula media 30 alunos
for cont in range(1,31):
    print('\n***Aluno {} ***' .format(cont))
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    media = (n1 + n2) / 2
    print("Media das notas {} e {} = {}" .format(n1,n2,media))
