phr = str(input('Digite uma frase: ')).strip().upper()
words = phr.split()
tog = ''.join(words)
inverse = ''
for litter in range(len(tog) - 1, -1, -1):
    inverse += tog[litter]
print('O inverso de {} é {}'.format(tog, inverse))
if tog == inverse:
    print('A frase é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')