intervalo1 = int(input('Digite o valor do primeiro intervalo: '))
intervalo2 = int(input('Digite o valor do segundo intervalo: '))

if (intervalo1 > intervalo2) :
    troca = intervalo1
    intervalo1 = intervalo2
    intervalo2 = troca

while (intervalo1 <= intervalo2) :
    if (intervalo1 % 2 == 0) :
        print(intervalo1)
    intervalo1 = intervalo1 + 1