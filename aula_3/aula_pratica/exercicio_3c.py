print('1 - Norte')
print('2 - Sul')
print('3 - Leste')
print('4 - Oeste')
escolha = int(input('Escolha uma zona: '))

escapou = False

if (escolha == 1 or escolha == 2 or escolha == 3) :
    escapou = True

if (escapou == True) :
    print('Você escapou!')
