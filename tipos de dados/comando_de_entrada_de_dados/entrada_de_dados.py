nome = input('Entre com seu nome: ')
print('Seu nome é: ', nome)
print(type(nome))

# Tipo de dado armazenado
idade = input('Entre com sua idade: ')
print('Sua idade é: ', idade)
print(type(idade))

# Formatando a saida.
base = float(input('Entre com um valor para base: '))
expoente = float(input('Entre com um valor para ser o expoente: '))
resultado = base ** expoente
print(str(base) + '^' + str(expoente), '=', resultado)
print(' %1.2f ^%1.2f = %1.4f' %(base, expoente, resultado))