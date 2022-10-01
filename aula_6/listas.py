mochila = ('Mochila', 'Camisa', 'Bacon', 'Abacate')
print('Tupla: ', mochila)

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = 'Laranja' #As listas são mutaveis
print('Lista: ', mochila)

#Manipulando Listas
mochila.append('Ovos') #Adiciona no último índice
print('Lista: ', mochila)

mochila.insert(1, 'Canivete')
print('Lista: ', mochila) #Adição do elemento no índice 1

del mochila[1] #excluir o elemento no índice 1
print('Lista: ', mochila)
mochila.remove('Ovos') #remove o elemento Ovos
print('Lista: ', mochila)