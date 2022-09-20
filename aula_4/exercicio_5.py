par = 0
for i in range(1, 101, 1) :
    if (i % 2 == 0) :
        par = par + i

media = par / 50

print('A média = %.2f' %media)