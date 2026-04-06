#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade se
#ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
#O programa deve informar o tempo que falta ou que passou do prazo.

from datetime import date
year = int(input('Ano de nascimento: '))
ty = date.today().year
age = ty - year
print('Quem nasceu em {} tem {} anos em {}.'.format(year, age, ty ))
if age == 18:
    print('Você tem que se alistar imediatamente!!')
elif age > 18:
    print('Você deveria ter se alistado há {} anos.'.format(ty - (year + 18)))
    print('Seu alistamento foi em {}'.format(year + 18))
else:
    print('Ainda faltam {} para o seu alistamento militar'.format(18 - age))
    print('Seu alistamento será em {}.'.format(year + 18))