#Escreva um programa para aprovar o empréstimo bancário para a compra
#de uma casa. Pergunte o valor da casa, o salário do complador e em quantas
#anos ele vai pagar.
#A prestação mensal naõ pode exceder 30% do salário ou então o emprestimo será negado
price = float(input('Valor da casa: R$'))
wage = float(input('Salário do comprador: R$'))
time = int(input('Quantos anos de financiamento? '))
installments = price/(time*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}.'.format(price, time, installments))
if installments >= 0.3*wage:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')