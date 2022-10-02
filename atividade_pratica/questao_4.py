def exibeMenu():
    print('Bem-vindo ao Controle de Funcionários do Lucas Pereira de Lima')
    print('------------------------------|Menu Principal|------------------------------')
    print('Opção 1 - Cadastrar Funcionário')
    print('Opção 2 - Consultar Funcionário(s)')
    print('Opção 3 - Remover Funcionário(s)')
    print('Opção 4 - Sair')
    print('----------------------------------------------------------------------------')

    while (True):
        try:
            opcao = int(input('Digite a opção desejada: '))
            break
        except ValueError:
            print('Dígito inválido!\nDigite somente as opções existentes.')

    if (opcao == 1) :
        cadastrarFuncionario(id)
    elif (opcao == 2) :
        consultarFuncionario()


def cadastrarFuncionario(id):
    global funcionarios

    funcionario = {}
    funcionarios = []
    id = 101

    funcionario['id'] = id
    funcionario['nome'] = input('Digite o nome do funcionário: ')
    funcionario['setor'] = input('Digite o setor do funcionário: ')
    funcionario['salario'] = input('Digite o salário do funcionário: ')
    print('Funcionário Cadastrado com Sucesso!')
    funcionarios.append(funcionario.copy())
    id += 1

    exibeMenu()

def consultarFuncionario() :
    print('------------------------------|Menu Consultar Funcionário|------------------------------')
    print('Opção 1 - Consultar Todos os Funcionários')
    print('Opção 2 - Consultar Funcionário(s) por ID')
    print('Opção 3 - Consultar Funcionário(s) por Setor')
    print('Opção 4 - Retornar')
    print('----------------------------------------------------------------------------')

    while (True):
        try:
            opcao = int(input('Digite a opção desejada: '))
            break
        except ValueError:
            print('Dígito inválido!\nDigite somente as opções existentes.')

    if (opcao == 1) :
        for f in funcionarios:
            for i, j in f.items():
                print('{}:{}'.format(i, j))


        exibeMenu()

exibeMenu()