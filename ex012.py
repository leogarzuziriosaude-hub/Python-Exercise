#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
n = float(input('Parabéns!! Você ganhou 5% de desconto na sua próxima compra, qual foi o valor da sua compra? R$'))
print('Se a sua compra custou {:.2f} reais, com 5% de desconto, o novo valor da sua compra é {:.2f} reais.'.format(n, n*0.95))
