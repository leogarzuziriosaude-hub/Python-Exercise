#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
C = float(input('Digite alguma temperatura em °C: '))
print('{:.2f} °C equivalem a {:.2f} °F'.format(C, (9*C/5) + 32))
