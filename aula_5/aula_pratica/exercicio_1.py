def calculaFatorial(numero) :
    """
    Função para calcular fatorial de número.
    :param numero: Número inserido pelo usuário.
    :return: Retorna o fatorial do número inserido.
    """
    fatorial = 1
    while (numero > 1):
        fatorial *= numero
        numero -= 1
    return print('O fatorial é {}' .format(fatorial))

def validaDados(numero) :
    while (numero < 0) :
        numero = int(input('Por favor digite um número positivo: '))

    calculaFatorial(numero)

def inseriNumero() :
    numero = int(input('Digite um número: '))
    return validaDados(numero)

inseriNumero()
help(calculaFatorial)