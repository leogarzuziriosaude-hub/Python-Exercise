#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa 60 reais por dia e 0,15 centavos por km rodado.
k = float(input('Quantos km rodados? '))
d = int(input('Quantos dias alugado? '))
print('O total a pagar é de {:.2f}'.format(60 * d + 0.15 * k))
