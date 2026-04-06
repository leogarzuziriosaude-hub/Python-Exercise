ncount = 0
sum = 0
for n in range(1, 500):
    if n % 3 == 0 and n % 2 == 1:
        ncount += 1
        sum += n
print('A soma de todos os {} valores solicitados é {}.'.format(ncount, sum))
