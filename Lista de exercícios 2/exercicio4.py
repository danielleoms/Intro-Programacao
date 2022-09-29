# 7.	 Seja a seguinte série: 1, 4, 9, 16, 25, 36, ... Escreva um programa que gere esta série até o N-ésimo termo, digitado pelo usuário.

n = int(input("Quantos números você quer que a sequência tenha? "))
S = 1
print("A sequência é", S, end="")
for cont in range(1, n):
    S += (2 * cont) + 1
    print(f", {S}", end="")
