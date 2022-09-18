valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

if (valor1 != 0 and valor2 != 0 and valor3 != 0) :
   if (valor1 < valor2 + valor3 and (valor2 < valor1 + valor3) and (valor3 < valor1 + valor2)) :
       if ((valor1 == valor2 and valor1 == valor3) and valor2 == valor3):
           print('Equilátero')
       elif (valor1 == valor2 or valor2 == valor3):
           print('Isósceles')
       else:
           print('Escaleno')
   else :
       print('Um lado não pode ser maior que a soma dos outros dois!')
else :
    print('Nenhum lado pode ser 0!')