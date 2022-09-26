print('Bem-vindo a sorveteria do Lucas Pereira de Lima')
print('-------------------------------------------Cardápio--------------------------------------------')
print('| Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |')
print('-----------------------------------------------------------------------------------------------')

#Variável acumuladora dos preços dos sorvetes
precoTotal = 0.0

while (True) : #Estrutura de repetição irá se repetir enquanto for verdadeira
    #Recebendo dados do tamanho do pote de sorvete e o código do sorvete
    tamanhoPote = input('Digite o tamanho do pote de sorvete desejado (P, M ou G): ')
    codigoSorvete = input('Digite o código do sorvete desejado (TR, ES ou PR): ')

    #Verificando se o tamanho e código digitados não conferem
    if (tamanhoPote != 'P' and tamanhoPote != 'M' and tamanhoPote != 'G' or codigoSorvete != 'TR' and codigoSorvete != 'ES' and codigoSorvete != 'PR'):
        print('TAMANHO ou CÓDIGO inválido(s)!!!')
        continue #irá repetir até a condição ser falsa
    else: #caso conferem entrarão nesta condição
        if (tamanhoPote == 'P') : #Verifica se o tamanho é igual a P
               if (codigoSorvete == 'TR') : #Verifica se o código é TR
                   #Atribuição nas variáveis
                   codigo = 'TR'
                   descricao = 'Sabor Tradicional'
                   tamanho = 'P'
                   preco = 6.00
                   precoTotal += preco #Acumulando o valor

               elif (codigoSorvete == 'ES') : #Verifica se o código é ES
                   codigo = 'ES'
                   descricao = 'Sabor Especial'
                   tamanho = 'P'
                   preco = 7.00
                   precoTotal += preco

               else:
                   codigo = 'PR'
                   descricao = 'Sabor Premium'
                   tamanho = 'P'
                   preco = 8.00
                   precoTotal += preco

        elif (tamanhoPote == 'M') : #Verifica se o tamanho é igual a M
            if (codigoSorvete == 'TR'):
                codigo = 'TR'
                descricao = 'Sabor Tradicional'
                tamanho = 'M'
                preco = 10.00
                precoTotal += preco

            elif (codigoSorvete == 'ES'):
                codigo = 'ES'
                descricao = 'Sabor Especial'
                tamanho = 'M'
                preco = 12.00
                precoTotal += preco

            else:
                codigo = 'PR'
                descricao = 'Sabor Premium'
                tamanho = 'M'
                preco = 14.00
                precoTotal += preco

        elif (tamanhoPote == 'G') : #Verifica se o tamanho é igual a G
            if (codigoSorvete == 'TR'):
                codigo = 'TR'
                descricao = 'Sabor Tradicional'
                tamanho = 'G'
                preco = 18.00
                precoTotal += preco

            elif (codigoSorvete == 'ES'):
                codigo = 'ES'
                descricao = 'Sabor Especial'
                tamanho = 'G'
                preco = 21.00
                precoTotal += preco

            else:
                codigo = 'PR'
                descricao = 'Sabor Premium'
                tamanho = 'G'
                preco = 24.00
                precoTotal += preco

    print('Você pediu o sorvete {} {} de R$ %.2f' .format(descricao, tamanho) %preco)

    opcao = input('Deseja pedir algo mais? (S/N): ')

    if (opcao == 'S') : #Verifica se o usuário deseja continuar
        continue
    elif (opcao == 'N') :
        print('O total a ser pago é: R$ %.2f' %precoTotal)
        break
    else :
        print('Opção inválida!!')
        continue