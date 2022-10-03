cadastro = {
    'nome': [],
    'sexo': [],
    'ano': [],
    'idade': []
}

contador = 0
media = 0
contadorIdade = 0

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break

    nome = input('Qual é o seu nome: ')
    sexo = input('Qual é o seu sexo: [M/F]')
    ano = int(input('Qual é o seu ano de nascimento?'))
    idade = 2022 - ano

    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)
    contadorIdade = contadorIdade + idade
    contador += 1

media = contadorIdade / contador
print(cadastro)
print('Total de cadastros: {}'.format(contador))
print('Média de idades: {}'.format(media))
print('Lista de mulheres com menos de 30 anos:')
for i, j in cadastro:
    print(cadastro.items())

print('Lista de homens com idade maior que a média:')
