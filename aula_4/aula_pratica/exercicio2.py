while (True) :
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')

    escolha = int(input('Digite a operação desejada: '))

    if (escolha == 1):
        soma = valor1 + valor2
        print('{} + {} = {}'.format(valor1, valor2, soma))
    elif (escolha == 2):
        subtracao = valor1 - valor2
        print('{} - {} = {}'.format(valor1, valor2, subtracao))
    elif (escolha == 3):
        multiplicacao = valor1 * valor2
        print('{} x {} = {}'.format(valor1, valor2, multiplicacao))
    elif (escolha == 4):
        multiplicacao = valor1 / valor2
        print('{} / {} = {}'.format(valor1, valor2, multiplicacao))
    elif (escolha == 5):
        print('Tchau, tchau!')
        break
    else:
        print('Opção inválida!')