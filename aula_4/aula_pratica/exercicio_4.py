while (True) :
    idade = int(input('Digite a idade: '))

    if (idade < 3):
        precoIngresso = 0.0
        print('Preço do ingresso: R$ %.2f' % precoIngresso)
    elif (idade >= 3 and idade <= 12):
        precoIngresso = 15.00
        print('Preço do ingresso: R$ %.2f' % precoIngresso)
    else:
        precoIngresso = 30.00
        print('Preço do ingresso: R$ %.2f' % precoIngresso)

    escolha = int(input('Deseja adicionar outra idade?\n1 - Sim\n2 - Não\nDigite: '))

    if (escolha == 1) :
        continue
    elif (escolha == 2) :
        break
    else :
        print('Opção inválida!')
        continue