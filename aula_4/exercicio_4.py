while True :
    nome = input('Nome: ')
    senha = input('Senha: ')

    if (nome != 'Lucas' or senha != 'admin') :
        print('Usuário inválido!')
        continue
    else :
        print('Logado com sucesso!')
        break