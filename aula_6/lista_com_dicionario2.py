game = {}
games = []
for i in range(3):
    game['nome'] = input('Qual o nome do jogo: ')
    game['videogame'] = input('Para qual video-game ele foi lançado: ')
    game['ano'] = input('Qual ano de lançamento: ')
    games.append(game.copy())

    print('-' * 20)

for e in games:
    for i, j in e.items():
        print('O campo {} tem o valor {}'.format(i, j))