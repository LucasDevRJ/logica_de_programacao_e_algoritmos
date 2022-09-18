quantidadeKwhConsumida = float(input('Digite a quantidade de kWh consumida: '))
print('R - residência')
print('I - industria')
print('C - comércio')
tipoInstalacao = input('Digite o tipo de instalação: ')

if (tipoInstalacao == 'R') :
    if (quantidadeKwhConsumida <= 500) :
        preco = 0.40
        precoTotal = quantidadeKwhConsumida * preco
    else :
        preco = 0.65
        precoTotal = quantidadeKwhConsumida * preco
elif (tipoInstalacao == 'I') :
    if (quantidadeKwhConsumida <= 100) :
        preco = 0.55
        precoTotal = quantidadeKwhConsumida * preco
    elif (quantidadeKwhConsumida > 1000) :
        preco = 0.60
        precoTotal = quantidadeKwhConsumida * preco
elif (tipoInstalacao == 'C') :
    if (quantidadeKwhConsumida <= 5000) :
        preco = 0.55
        precoTotal = quantidadeKwhConsumida * preco
    else :
        preco = 0.60
        precoTotal = quantidadeKwhConsumida * preco
else :
    print('Opção inexistente!')

print('Quantidade consumida: {} kWh' .format(quantidadeKwhConsumida))
print('Tipo de instalação: ' + tipoInstalacao)
print('Preço do kWh: R$ {}' .format(preco))
print('Preço Total: R$ {}' .format(precoTotal))