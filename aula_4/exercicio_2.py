contador = 0
notas = 0

while (contador < 5) :
    nota = float(input('Digite a {}º nota: ' .format(contador + 1)))
    notas = notas + nota
    contador = contador + 1

media = notas / contador
print('Media final: %.2f' %media)