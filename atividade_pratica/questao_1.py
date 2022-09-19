print('Bem-vindo a Loja do Lucas Pereira de Lima')
valorProduto = float(input('Digite o valor do produto: '))
quantidadeProduto = int(input('Digite a quantidade do produto: '))

if (quantidadeProduto < 0 or valorProduto < 0.0) :
    print('Digite preço e/ou quantidade válido(s)!')
else :
    if (quantidadeProduto >= 0 and quantidadeProduto < 11):
        custoEmbalagem = 30.00
    elif (quantidadeProduto >= 11 and quantidadeProduto < 101):
        custoEmbalagem = 60.00
    elif (quantidadeProduto >= 101 and quantidadeProduto < 1001):
        custoEmbalagem = 120.00
    else:
        custoEmbalagem = 240.00

# cálculos com desconto e sem desconto
valorSemCustos = valorProduto * quantidadeProduto
valorComCustos = valorProduto * quantidadeProduto * custoEmbalagem
print()
print('Valor total sem os custos: R$ %.2f' %valorSemCustos)
print('Valor total com os custos: R$ %.2f' %valorComCustos)
