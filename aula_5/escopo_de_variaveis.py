def comida() :
    print(ovos)

ovos = 12 #variável global
comida()

def comida() :
    ovos = 12 #variável local
    bacon()
    print(ovos)

def bacon() :
    ovos = 6

comida()

def comida() :
    ovos = 'Variável local de comida'
    print(ovos)

def bacon() :
    ovos = 'Variável local de bacon'
    print(ovos)
    comida()
    print(ovos)

ovos = 'Variável global'
bacon()
print(ovos)

def comida() :
    global ovos
    ovos = 'comida'

ovos = 'global'
comida()
print(ovos)