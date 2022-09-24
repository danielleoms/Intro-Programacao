# Elaborar um programa que solicita a entrada de 3 valores (a, b, c) e verifica se esses valores podem formar ou não um triângulo.
# Você deve considerar que os valores lidos são inteiros e positivos.
# Caso os valores formem um triângulo, exiba essa informação e o valor do perímetro deste triângulo. Se não formarem triângulo, apenas exiba uma mensagem com essa informação.
# (Obs.: Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados.)

a = int(input('Informe o valor de a:'))
b = int(input('Informe o valor de b:'))
c = int(input('Informe o valor de c:'))

if  a < b + c and b < c + a and c < b + a:
    print('Os valores podem formar um triângulo e o perimêtro é {}' .format(a+b+c))

else:
    print('Não pode formar um triângulo')
