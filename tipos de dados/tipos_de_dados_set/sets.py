# Conjuntos 
# Mutaveis
# Desordenadas
# Sem elementos duplicados
# Criando conjunto set em python
conjunto_a = set()
print('conjunto vazio:')
print(conjunto_a)
print(type(conjunto_a))

# criando um conjunto via string
conjunto_a = set('python')
print('conjunto com uma string:')
print(conjunto_a) # vai imprimir de forma desordenada
                  # {'o', 'y', 'n', 't', 'p', 'h'}

# Criando set utilizando lista
conjunto_a = set(['IGTI', 'MBA', 'IGTI']) # como podemos ver nos criamos elementos iguais, mas o set não vai imprimir os duplicados
print('conjunto via lista:')
print(conjunto_a)

# Criando um conjunto com varios tipos diferentes.
conjunto_a = set([1, 2, 'IGTI', 4, 'Bootcamp', 6, 'MBA'])
print('Conjunto com valores de tipos diferentes:')
print(conjunto_a)
print(type(conjunto_a))

# Adicionando elementos a um conjunto com o add 'Adciona um elemento de cada vez'
conjunto_a.add(8)
conjunto_a.add(9)
conjunto_a.add((6, 7))
print('conjunto após a adição de valores:')
print(conjunto_a)

# Adicionando elementos através da função update.
conjunto_a.update([10, 11]) # Adicionando uma lista de elementos.
print('Adicionando valores com a função update():')
print(conjunto_a)

# Como não são ordenados não podemos acessar via indice !!!
# Criando conjunto
conjunto_a = set(['IGTI', 'Bootcamp', 'Python'])
print('Conjunto inicial:')
print(conjunto_a)

# Acessando elementos através de um loop.
print('Elementos do conjunto A:')
for i in conjunto_a:
    print(i, end = ' ')

# Verificando se um elemento está presente ao conjunto
print('IGTI' in conjunto_a)

# Removendo elementos de um conjunto.
# Criando o conjunto
conjunto_a = set([1, 2, 3, 4, 5, 6,
                  7, 8, 9, 10, 11, 12])
print('Conjunto inicial:')
print(conjunto_a)

# Removendo com a função remove.
conjunto_a.remove(5)
conjunto_a.remove(6)
print('Conjunto apos a remoção com a função remove():')
print(conjunto_a)

# Removendo com a função discard.
conjunto_a.discard(8)
conjunto_a.discard(9)
print('Conjunto após a remoção com a função discard():')
print(conjunto_a)

# Removendo com a função pop.
conjunto_a.pop() # remove o 1 item.
print('Conjunto após a remoção com a função pop():')
print(conjunto_a)

# Removendo com a função clear.
conjunto_a.clear()
print('Removendo todos os elementos do conjunto com clear():')
print(conjunto_a)