# São parecidas com as lista porem usa-se ()com algumas particularidades
# São imutáveis
# Varios tipos de elementos

# Criando uma tupla vazia
tupla_1 = ()
print('Tupla vazia: ')
print(tupla_1)
print(type(tupla_1))

# Criando uma tupla com string
tupla_1 = ('IGTI', 'Python')
print('Tupla utilizando string: ')
print(tupla_1)

# Criando uma tupla atraves de uma lista.
lista_1 = [1, 2, 3, 4, 5, 6]
print(type(lista_1))
print('Tupla através de uma lista:')
print(tuple(lista_1))
print(type(tuple(lista_1)))

# Criando uma tupla através da palvra tuple()
tupla_1 = tuple('IGTI')
print('tupla crianda através da palavra tuple():')
print(tupla_1)

# Criando tuplas aninhadas.
tupla_1 = (0, 1, 2, 3)
tupla_2 = ('python', 'IGTI')
tupla_3 = (tupla_1, tupla_2) # cria uma tupla com duas tuplas dentro
print('Tuplas aninhadas:')
print(tupla_3)

# Criando uma tupla através da função
tupla_1 = tuple([1, 2, 3, 4, 5])
# Acessando o elemento através do indice.
print('primeiro elemento da tupla:')
print(tupla_1[0])
# Acessando o ultimo ellemento da tupla.
print('ultimo elemento da tupla:')
print(tupla_1[-1])
# Encontrando o penultimo elemento da tupla.
print('Encontrando o ultimo elemento da tupla:')
print(tupla_1[-2])