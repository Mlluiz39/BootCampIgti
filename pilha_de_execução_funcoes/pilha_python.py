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


# Com esse codigo podemos ver a pinha( stack) em execução usando debug

def soma_dois_numeros(a, b):
    resultado = a + b
    return resultado

def multiplica_dois_numeros(c, d):
    resultado = c * d
    return resultado

soma = soma_dois_numeros(10, 51)
print(soma)
multiplica = multiplica_dois_numeros(5, 8)
print(multiplica)