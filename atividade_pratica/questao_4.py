codigoFuncionario = 0  # Contador da ID
funcionarios = []  # Lista de funcionários com chaves dentro


def cadastrarFuncionario(id):  # função para cadastrar funcionário
    print('------------------------------|Cadastrar Funcionário|------------------------------')

    print('O código do funcionário {}'.format(id))
    # Pegando dados do usuário
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor do funcionário: ')
    salario = float(input('Digite o salário do funcionário: '))

    funcionario = {  # Criação das chaves para cada funcionário
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }

    funcionarios.append(funcionario.copy())  # adicionando o funcionário na lista


def consultarFuncionario():
    while (True):  # estrutura de repetição para o menu
        print('------------------------------|Menu Consultar Funcionário|------------------------------')
        print('Opção 1 - Consultar Todos os Funcionários')
        print('Opção 2 - Consultar Funcionário(s) por ID')
        print('Opção 3 - Consultar Funcionário(s) por Setor')
        print('Opção 4 - Retornar')
        print('----------------------------------------------------------------------------')

        try:  # Tratamento de dados errados
            opcao = int(input('Digite sua opção desejada: '))  # Escolha do usuário no menu

            if (opcao == 4):  # Retorno
                break

            if (len(funcionarios) > 0):  # Verifica se tem algum funcionário na lista

                if (opcao == 1):
                    for funcionario in funcionarios:  # laço para percorrer a lista
                        for key, value in funcionario.items():  # pega a chave o conteúdo das chaves
                            print('{} : {}'.format(key, value))

                elif (opcao == 2):
                    funcionarioId = int(input('Digite o ID do funcionário que deseja consultar: '))

                    for funcionario in funcionarios:
                        if (funcionario['id'] == funcionarioId):
                            for key, value in funcionario.items():
                                print('{} : {}'.format(key, value))

                elif (opcao == 3):
                    funcionarioSetor = input('Digite o setor do funcionário que deseja consultar: ')

                    for funcionario in funcionarios:
                        if (funcionario['setor'] == funcionarioSetor):
                            for key, value in funcionario.items():
                                print('{} : {}'.format(key, value))
            else:
                print('Nenhum funcionário foi cadastrado!')

        except ValueError:  # tratando erro do código
            print('Digito inválido!!\nDigite somente números válidos!')

def removerFuncionario():
    if (len(funcionarios) > 0):
        try:
            print('------------------------------|Remover Funcionário|------------------------------')
            codigoFuncionario = int(input('Digite o código do funcionário que deseja remover: '))

            for funcionario in funcionarios:
                if (funcionario['id'] == codigoFuncionario):
                    funcionarios.remove(funcionario)
                    print('Removido com sucesso!')
                else:
                    print('ID inválida!!')
            print('----------------------------------------------------------------------------')
        except ValueError:
            print('Dígito inválido!\nDigite somente as opções existentes.')
    else:
        print('Nenhum funcionário foi cadastrado!')

while (True):
    print('Bem-vindo ao Controle de Funcionários do Lucas Pereira de Lima')
    print('------------------------------|Menu Principal|------------------------------')
    print('Opção 1 - Cadastrar Funcionário')
    print('Opção 2 - Consultar Funcionário(s)')
    print('Opção 3 - Remover Funcionário(s)')
    print('Opção 4 - Sair')
    print('----------------------------------------------------------------------------')

    try:
        opcao = int(input('Digite a opção desejada: '))

        if (opcao == 1):
            codigoFuncionario = codigoFuncionario + 1
            cadastrarFuncionario(codigoFuncionario)
        elif (opcao == 2):
            consultarFuncionario()
        elif (opcao == 3):
            removerFuncionario()
        elif (opcao == 4):
            print('Tchau, tchau')
            break

    except ValueError:
        print('Dígito inválido!\nDigite somente as opções existentes.')