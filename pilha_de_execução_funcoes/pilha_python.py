# função que inverte o valor da string passada

def inverte_string(valor_string):
    resultado = ' '
    for caracter in valor_string:
        resultado = caracter + resultado

    return resultado

    string = input('Entre com alguma string: ')
    while string.strip() != '':
        print('O inverso da ', string, 'é', inverte_string(string))
        string = input('Entre com outra string ou presione ENTER para sair: ')