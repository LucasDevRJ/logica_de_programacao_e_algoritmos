s1 = 'Algoritmos'
print(s1)
#s1[0] = 'a'

s1 = list('Algoritmos')
print(s1) #print separado
print(''.join(s1)) #print agrupado

s1[0] = 'a'
print(''.join(s1))

s2 = 'Lógica de Programação e Algoritmos'
print(s2.startswith('Lógica')) #verifica se começa com a string
print(s2.startswith('Algoritmos')) #verifica se termina com a string
print(s2.lower()) #converte tudo para minusculo
print(s2.upper()) #converte tudo para maiusculo
print(s2.count('a')) #conta a quantidade de tal caracter
print(s2.split(' ')) #quebra a string com um espaço]
print(s2.replace('Programação', 'Desenvolvimento')) #substitui strings

