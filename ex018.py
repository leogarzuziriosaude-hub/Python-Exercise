#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente.
from math import sin, cos, tan, radians
a = float(input('Digite um ângulo: '))
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'
      .format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
