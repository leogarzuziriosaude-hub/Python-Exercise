a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and c == a:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('Os segmentos acima PODEM FORMAR um triângulo ISOSCELES.')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
