#Escreva um programa que leia a velocidade de um caro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite.
vel = int(input('Qual é a velocidade atual do carro? '))
multa = (vel - 80)*7
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    print('Você deverá pagar uma multa de {} reais!'.format(multa))
else:
    print('Sua velocidade está dentro do permitido.')
print('Tenha um bom dia! Dirija com segurança!')