nome = str(input('Digite um nome: '))
idade = int(input('Digite uma idade: '))

if (nome == 'Vinicius') :
    print('O nome é Vinicius')

elif (nome != 'Vinicius') :
    if (idade < 18) :
        print('É de menor')
    elif (idade > 100) :
        print('Essa pessoa não existe')