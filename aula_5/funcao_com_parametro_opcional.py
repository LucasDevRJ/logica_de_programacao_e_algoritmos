def soma3(x, y, z) :
    res = x + y + z
    print(res)

def soma3(x = 0, y = 0, z = 0) :
    res = x + y + z
    print(res)

soma3(1, 2, 3)
soma3(1, 2) #z foi omitido
soma3(1) #y e z foram omitidos
soma3() #x, y e z foram omitidos
