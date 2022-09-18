valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
operacao = int(input('Digite a operação desejada: '))

if (operacao == 1) :
    calculo = valor1 + valor2
    print('{} + {} = {}' .format(valor1, valor2, calculo))
elif (operacao == 2) :
    calculo = valor1 - valor2
    print('{} - {} = {}'.format(valor1, valor2, calculo))
elif (operacao == 3) :
    calculo = valor1 * valor2
    print('{} x {} = {}'.format(valor1, valor2, calculo))
elif (operacao == 4) :
    calculo = valor1 / valor2
    print('{} / {} = {}'.format(valor1, valor2, calculo))