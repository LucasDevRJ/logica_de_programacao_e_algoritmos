def validaString(frase, numeroMinimo, numeroMaximo) :
    if (len(frase) >= numeroMinimo and len(frase) <= numeroMaximo) :
        return print('Verdadeiro')
    else :
        return print('Falso')

validaString('Lucas', 1, 5)
validaString('Ana', 1, 2)