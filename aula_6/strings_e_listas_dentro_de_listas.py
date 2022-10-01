mochila = ['Mochila', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0])

#acessando letras
print(mochila[0][0])
print(mochila[2][1])

for item in mochila:
    for letra in item:
        print(letra, end='')
    print()

