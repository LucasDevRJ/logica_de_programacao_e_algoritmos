totalCompras = 0
valorArrecadado = 0.0
somaIdades = 0
mediaIdades = 0.0
contadorPessoas = 0

while (True):
    idade = int(input('Digite a idade: '))
    contadorPessoas += 1

    if (idade < 3):
        precoIngresso = 0.0
        print('Preço do ingresso: R$ %.2f' % precoIngresso)
        somaIdades += idade

    elif (idade >= 3 and idade <= 12):
        precoIngresso = 15.00
        print('Preço do ingresso: R$ %.2f' % precoIngresso)
        totalCompras += 1
        valorArrecadado += precoIngresso
        somaIdades += idade

    else:
        precoIngresso = 30.00
        print('Preço do ingresso: R$ %.2f' % precoIngresso)
        totalCompras += 1
        valorArrecadado += precoIngresso
        somaIdades += idade

    escolha = int(input('Deseja adicionar outra idade?\n1 - Sim\n2 - Não\nDigite: '))

    if (escolha == 1):
        continue
    elif (escolha == 2):
        mediaIdades = somaIdades / contadorPessoas
        print('Total pagantes: ', totalCompras)
        print('Valor arrecadado: R$ %.2f' % valorArrecadado)
        print('Média de idades: %.2f' % mediaIdades)
        break
    else:
        print('Opção inválida!')
        continue
