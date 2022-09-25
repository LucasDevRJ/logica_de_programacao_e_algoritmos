while (True):
    valor = int(input('Digite um valor monetário: R$ '))

    if (valor >= 100):
        numeroCedulas = valor // 100
        print('Quantidade de cédulas de R$ 100,00 necessárias para pagar o valor: %.0f' % numeroCedulas)
        valor -= 100 * numeroCedulas

    if (valor >= 50):
        numeroCedulas = valor // 50
        print('Quantidade de cédulas de R$ 50,00 necessárias para pagar o valor: %.0f' % numeroCedulas)
        valor -= 50 * numeroCedulas

    if (valor >= 20):
        numeroCedulas = valor // 20
        print('Quantidade de cédulas de R$ 20,00 necessárias para pagar o valor: %.0f' % numeroCedulas)
        valor -= 20 * numeroCedulas

    if (valor >= 10):
        numeroCedulas = valor // 10
        print('Quantidade de cédulas de R$ 10,00 necessárias para pagar o valor: %.0f' % numeroCedulas)
        valor -= 10 * numeroCedulas

    if (valor >= 5):
        numeroCedulas = valor // 5
        print('Quantidade de cédulas de R$ 5,00 necessárias para pagar o valor: %.0f' % numeroCedulas)
        valor -= 5 * numeroCedulas

    if (valor >= 1):
        numeroCedulas = valor // 1
        print('Quantidade de cédulas de R$ 1,00 necessárias para pagar o valor: %.0f' % numeroCedulas)
        valor -= 1 * numeroCedulas

    resposta = int(input('Deseja continuar?\n1 - Sim\n2 - Não\nDigite: '))
    if (resposta == 1):
        continue
    elif (resposta == 2):
        print('Tchau, tchau')
        break
