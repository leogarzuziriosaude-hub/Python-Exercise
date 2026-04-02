#Escreva um programa que pergunte o salário de um funcionário e calcule
#o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
#aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
wage = float(input('Qual é o salário do funcionário? R$'))
if wage > 1250:
    new = wage * 1.10
else:
    new = wage * 1.15
print('Quem ganhava R${:.2f} passará a ganhar R${:.2f} agora.'.format(wage, new))
