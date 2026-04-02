#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 para viagens mais longar.
km = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f} Km.'.format(km))
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}.'.format(0.50*km))
else:
    print('E o preço da sua passagem será de R${:.2f}.'.format(0.75*km))
