precoProduto = float(input('Digite o preço do produto: '))
percentualDesconto = float(input('Digite o percentual de desconto do produto: '))

calculo = precoProduto - (precoProduto * percentualDesconto / 100)

print('Valor do desconto: {}%'.format(percentualDesconto))
print('Preço final: R$ {}'.format(calculo))