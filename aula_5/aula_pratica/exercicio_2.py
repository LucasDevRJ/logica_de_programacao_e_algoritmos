def criaArquivo(arquivo) :
    try :
        criaArquivo = open(arquivo, 'wt+')
        criaArquivo.close()
    except :
        print('Erro na criação do documento')
    else :
        print('Arquivo {} foi criado!' .format(arquivo))

def verificaExistenciaArquivo(arquivo) :
    try:
        arquivoExistente = open(arquivo, 'rt')
        arquivoExistente.close()
    except FileNotFoundError:
        return False
    else :
        return True

arquivo = 'jogos.txt' #criação do arquivo para armazenar dados

if (verificaExistenciaArquivo(arquivo)) :
    print('Arquivo localizado!')
else :
    print('Arquivo inexistente!')
    criaArquivo(arquivo)

def cadastrarJogo() :
    jogo = input('Digite o nome do jogo: ')
    console = input('Digite o nome do console: ')
    try :
        abreArquivo = open(arquivo, 'at')
    except :
        print('Erro ao abrir arquivo')
    else :
        abreArquivo.write('Jogo: {}\nConsole: {}\n' .format(jogo, console))
    finally :
        abreArquivo.close()

def listarCadastro() :
    try:
        abreArquivo = open(arquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(abreArquivo.read())
    finally:
        abreArquivo.close()


while True :
    print('Menu')
    print('1 - Cadastrar jogo')
    print('2 - Listar cadastros')
    print('3 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1) :
        cadastrarJogo()
    elif (opcao == 2) :
        listarCadastro()
    elif (opcao == 3) :
        print('Encerrando programa')
        break
    else :
        print('Opção inválida!!')
