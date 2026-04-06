#Um programa que classifique da maneira
#até 9 anos = MIRIM
#até 14 anos = INFANTIL
#até 19 anos = JUNIOR
#até 25 anos = SÊNIOR
#acima : MASTER
from datetime import date
birt = int(input('Ano de Nascimento: '))
age = date.today().year - birt
print('O Atleta tem {} anos.'.format(age))
if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Classificação: INFANTIL')
elif age <= 19:
    print('Classificação: JUNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
