def metragem_limpeza() : #função para medir a metragem e devolver o valor dela total
    print('Bem-vindo ao programa de Serviços de Limpezas do Lucas Pereira de Lima')
    while True:
        print('Metragem (m²)                | Valor (R$)')
        print('Metragem entre 30 e 300 m²   | 60 x 30% x metragem')
        print('Metragem entre 300 e 700 m²  | 120 x 50% x metragem')

        try: #tratamento de dados não númericos
            metragem = float(input('Digite a metragem: '))
        except ValueError:
            print('Valor não númerico!!!')
            continue

        #verifica se o valor digitado da metragem esta entre 30 e 300 ou 300 e 700
        if (metragem >= 30 and metragem < 300):
            valorMetragem = 60 + 0.3 * metragem
            return tipo_limpeza(valorMetragem) #chama a função de limpeza
        elif (metragem >= 300 and metragem < 700):
            valorMetragem = 120 + 0.5 * metragem
            return tipo_limpeza(valorMetragem)
        else:
            print('Metragem inválida!!')
            continue

#função para devolver o tipo de limpeza e multiplicador, com passagem de parametro do valor da metragem
def tipo_limpeza(valorMetragem) :
    tipoLimpeza = ''
    print()
    #verifica se a limpeza é do tipo B ou C
    while (tipoLimpeza != 'B' and tipoLimpeza != 'C') :
        print('Tipo                                                               | Multiplicador')
        print('B – Básica - Indicada para sujeiras semanais ou quinzenais.        | 1.00')
        print('C – Completa - Indicada para sujeiras antigas e/ou não rotineiras. | 1.30')
        tipoLimpeza = str(input('Digite o tipo de limpeza desejada: '))

        if (tipoLimpeza == 'B') :
            valorLimpeza = 1.00 #atribui o multiplicador ao tipo de limpeza
            return adicional_limpeza(valorMetragem, valorLimpeza)
        elif (tipoLimpeza == 'C') :
            valorLimpeza = 1.30
            return adicional_limpeza(valorMetragem, valorLimpeza)
        else :
            print('Tipo inválido!!')

#função para adicionar os valores do serviços a mais com passagem do valor da metragem e limpeza
def adicional_limpeza(valorMetragem, valorLimpeza) :
    valorAdicional = 0.0
    while (True) :
        print()
        print('Adicionais                                   | Valor (R$)')
        print('0- Não desejo mais nada (encerrar)           | 0,00')
        print('1- Passar 10 peças de roupas - R$ 10.00      | 10,00')
        print('2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00 | 12,00')
        print('3- Limpeza de 1 Geladeira/Freezer - R$ 20,00 | 20,00')
        resposta = int(input('Deseja mais algum serviço adicional?\nDigite: '))

        #verifica a resposta digitada
        if (resposta == 1) :
            valorAdicional = valorAdicional + 10.00 #acumula valores
            print('Serviço adicionado!')
            continue
        elif (resposta == 2) :
            valorAdicional = valorAdicional + 12.00
            print('Serviço adicionado!')
            continue
        elif (resposta == 3) :
            valorAdicional = valorAdicional + 20.00
            print('Serviço adicionado!')
            continue
        elif (resposta == 0) :
            return calculaValorTotal(valorMetragem, valorLimpeza, valorAdicional)

#função para calcular o preço total
def calculaValorTotal(valorMetragem, valorLimpeza, valorAdicional) :
    print()
    valorTotal = (valorMetragem * valorLimpeza) + valorAdicional
    print('Total a ser pago: R$ %.2f' %valorTotal, '(metragem: %.2f' %valorMetragem,
    ' x tipo: %.2f' %valorLimpeza, ' + adicional: %.2f)' %valorAdicional)


metragem_limpeza() #chamada da função