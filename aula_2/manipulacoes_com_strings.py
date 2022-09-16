s1 = 'Lógica de Programação'
s1 = s1 + ' e Algoritmos'

print(s1)

# multiplicacao em vezes de asteristicos
s1 = 'A' + '-' * 10 + 'B'
print(s1)

# composição
nota = 8.5
s1 = 'Você tirou %f na disciplina de Algoritmos' %nota
print(s1)

# formatando a variável para duas casas decimais
s1 = 'Você tirou %.2f na disciplina de Algoritmos' %nota
print(s1)

# outra forma de formatar variáveis
disciplina = 'Algoritmos'
s1 = 'Você tirou %.2f na disciplina de %s' %(nota, disciplina)
print(s1)

# outra forma de formatação
s1 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)
print(s1)

# Fatiamento de String
s1 = 'Lógica de Programação e Algoritmos'
print(s1[0:6])
print(s1[24:34])
print(s1[:6])

# pegar tamanho da variável
tamanho = len(s1)
print(tamanho)