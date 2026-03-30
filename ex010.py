#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar. Considerar US$1,00 = R$3,27
n = float(input('Quantos reais você tem na sua carteira? '))
print('Com {} reais você consegue comprar {:.2f} dólares.'.format(n, n/3.27))
