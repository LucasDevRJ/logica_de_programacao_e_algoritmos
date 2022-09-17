materia1 = float(input('Digite a nota da primeira matéria:'))
materia2 = float(input('Digite a nota da segunda matéria:'))
materia3 = float(input('Digite a nota da terceira matéria:'))
media = (materia1 + materia2 + materia3) / 3

if (media > 7 or media == 7):
    print('O aluno está aprovado!')
else:
    print('O aluno está reprovado!')