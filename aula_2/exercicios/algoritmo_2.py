kmPercorridos = float(input('Digite a quantidade de KM percorridos: '))
diasAlugados = int(input('Digite a quantidade de dias que o carro foi alugado: '))

precoKmPercorridos = 0.15 * kmPercorridos
precoDiasAlugados = 60 * diasAlugados
precoTotal = precoKmPercorridos + precoDiasAlugados

print('O preço total é R$ {}'.format(precoTotal))