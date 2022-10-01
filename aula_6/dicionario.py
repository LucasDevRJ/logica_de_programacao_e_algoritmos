game = {'nome':'Super Mario',
        'desenvolvedora':'Nintendo',
        'ano':1990}
print(game)

#chamando dados a partir da chave
print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

print(game.values()) #retorna somente os dados
for i in game.values():
    print(i)

print(game.keys()) #retorna as chaves

for i in game.keys():
    print(i) #retorna as chaves

for i, j in game.items():
    print('{} = {}'.format(i, j))