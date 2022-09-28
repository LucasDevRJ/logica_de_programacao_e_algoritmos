#Erro de sintaxe
while True
    print('Olá Mundo!')

100 * (2 / 0) #Erro de divisão

x = int(input('Por favor divgite um número: '))

while True :
    try :
        x = int(input('Por favor divgite um número: '))
        break
    except ValueError:
        print('Ops! Número inválido')

def div() :
    try :
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Erro de divisão por zero')
    except :
        print('Erro')
    else :
        return res
    finally :
        print('Executará sempre')

print(div())