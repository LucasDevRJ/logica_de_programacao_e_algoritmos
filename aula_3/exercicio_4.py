print('----------|Cardápio|----------')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
print('------------------------------')

opcao = int(input('Digite a opção desejada: '))

if (opcao == 1 or opcao == 2 or opcao == 3) :
    unidades = int(input('Digite a quantidade desejada: '))
    if (opcao == 1) :
        precoFruta = 2.30
    else :
        if (opcao == 2) :
            precoFruta = 3.60
        else :
            if (opcao == 3) :
                precoFruta = 1.85
else :
    print("Opção inválida")

precoTotal = precoFruta * unidades
print('Preço total: R$ {}' .format(precoTotal))
