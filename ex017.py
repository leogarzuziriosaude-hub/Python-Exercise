#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
#retangulo e calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
print('Se o Cateto Oposto vale {} e o Cateto adjacente vale {}, então a hipotenusa vale {}'.format(co, ca, hypot(co, ca)))
