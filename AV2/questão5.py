# 5.	Frases malucas - Em algumas situações é preciso gerar textos aleatórios para teste (por exemplo para preencher o design de um site em construção) 
# Para este fim, escreva um programa que gere 5 textos aleatórios baseado nas listas de palavras abaixo:

import random
  
artigos = ['o', 'a', 'um', 'uma']
sujeitos = ['gato', 'cachorro', 'homem', 'mulher']
verbos = ['cantar', 'correr', 'pular', 'nadar']
adverbios = ['agarosamente', 'silenciosamente', 'bem', 'mal']

print("{} {} {} {}" .format(random.choice(artigos), random.choice(sujeitos), random.choice(verbos), random.choice(adverbios)))

# (opcional) Incremente o programa utilizando 2 estruturas de frases:
# (1) artigo, sujeito, verbo, adverbio 
# ou (2) artigo, sujeito, verbo. 
# Utilize a função random.randint() para escolher aleatoriamente entre as 2 estruturas.
print('-=-' * 10)
print('          OPCIONAL')
print('-=-' * 10)
escolha = random.randint(1, 2)

if escolha == 1:
    print("{} {} {} {}" .format(random.choice(artigos), random.choice(sujeitos), random.choice(verbos), random.choice(adverbios)))
else:
    print("{} {} {}" .format(random.choice(artigos), random.choice(sujeitos), random.choice(verbos)))
