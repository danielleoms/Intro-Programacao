# Uma seguradora de saúde está oferecendo um plano de saúde promocional em que todos os conveniados pagam R$ 100,00 mais um adicional, de acordo com sua idade:

idade = int(input('Informe sua idade:'))

if idade <= 10:
    print('O valor do seu plano é de R$ 160,00')

elif idade >= 10 and idade <= 30:
    print('O valor do seu plano é de R$ 190,00')

elif idade >= 30 and idade  <= 45:
    print('O valor do seu plano é de R$230,00')

elif idade >= 45 and idade <= 59:
    print('O valor do seu plano é de R$350,00')

else:
    print('O valor do seu plano é de R$500,00')
