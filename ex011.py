#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m².
n = float(input('Quantos metros de comprimento tem a sua parede? '))
n1 = float(input('Quantos metros de altura tem a sua parede? '))
print('Se a sua parede tem {:.2f} de comprimeito e {:.2f} de altura, ela tem {:.2f} m² e precisará de {:.2f} litros de tinta para pintá-la'.format(n, n1, n*n1, (n*n1)/2))
