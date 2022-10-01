#Variável composta
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

print(mochila[0]) #print do elemento 1 - índice 0
print(mochila[2]) #print do elemento 3 - índice 2
print(mochila[0:2]) #print do elemento 1 e 2 - índice 0 e 1
print(mochila[2:]) #print dos elementos a partir do índice 2
print(mochila[-1]) #print do último

#mochila[2] = 'Ovos' Não podemos alterar elementos utilizando a Tupla

for item in mochila:
    print('Na minha mochila tem: {}'.format(item))

adicao = ('Queijo', 'Canivete')
mochila_adicao = mochila + adicao

print("Mochila: ",mochila)
print("Elemento adicionais: ", adicao)
print("Mochila com elementos adicionais: ", mochila_adicao)

mochila_adicionada_inverso = adicao + mochila
print('Mochila ao inverso: ', mochila_adicionada_inverso)