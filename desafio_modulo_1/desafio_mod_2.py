def funcao_2(num):
    numero_anterior = 0
    for i in list(range(num)):
        resultado = numero_anterior + i
        print('Numero A', i, 'Numero B', numero_anterior, 'Resultado: ', resultado)
        numero_anterior = i
funcao_2(10, 5)