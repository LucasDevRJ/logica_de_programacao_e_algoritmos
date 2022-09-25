print('Bem-vindo a Loja do Lucas Pereira de Lima')

#Receber o valor ponto flutuante digitado pelo usuário
valorProduto = float(input('Digite o valor do produto: '))

#Receber o valor inteiro digitado pelo usuário
quantidadeProduto = int(input('Digite a quantidade do produto: '))

#Verifica se a quantidade ou o valor do produto é menor que 0
if (quantidadeProduto < 0 or valorProduto < 0.0) :
    print('Digite preço e/ou quantidade válido(s)!')
else : #Se não for menor que 0, irá para esta condição
    #Verifica se a quantidade do produto esta entre 0 e 10
    if (quantidadeProduto >= 0 and quantidadeProduto < 11):
        custoEmbalagem = 30.00
    #Verifica se a quantidade do produto esta entre 11 e 100
    elif (quantidadeProduto >= 11 and quantidadeProduto < 101):
        custoEmbalagem = 60.00
    #Verifica se a quantidade do produto esta entre 101 e 1000
    elif (quantidadeProduto >= 101 and quantidadeProduto < 1001):
        custoEmbalagem = 120.00
    else:
    #Se a quantidade for maior ou igual a 1001, irá parar nesta condição
        custoEmbalagem = 240.00

#Cálculo do frete, que se consiste em multiplicar o valor do produto pela quantidade
valorSemFrete = valorProduto * quantidadeProduto

#Cálculo do valor com frete, que se consiste em multiplicar o valor do produto pela
#quantidade mais o valor do custo da embalagem
valorComFrete = valorProduto * quantidadeProduto + custoEmbalagem

print()
print('Valor total sem o frete: R$ %.2f' %valorSemFrete)
print('Valor total após o frete: R$ %.2f' %valorComFrete, '(frete de R$ %.2f' %custoEmbalagem,')')