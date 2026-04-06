print('{}LOJAS GUANABARA{}'.format('='*10, '='*10))
price = float(input('Preço das compras: R$'))
form = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão de crédito
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito
Qual a sua opção de compra? '''))
if form == 1:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(price, 0.9 * price))
elif form == 2:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(price, 0.95 * price))
elif form == 3:
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(price / 2))
    print('Sua compra de R$ {:.2f} vai custar {:.2f} no final.'.format(price, price))
elif form == 4:
    option = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(option, price * 1.2 / option))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(price, 1.2 * price))
else:
    print('Opção de pagamento INVÁLIDA. Tente novamente.')
