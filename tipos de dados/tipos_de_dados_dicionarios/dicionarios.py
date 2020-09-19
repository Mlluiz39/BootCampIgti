# Dicionarios =
# Não ordenados
# Armazena o par de chave:valor
# As chaves não podem ser repitidas
# podem ser armazenados varios tipos de valores
# Criando um dicionario vazio
dicionario = {}
print(dicionario)
print(type(dicionario))

# Criando um dicionario com chave inteiras
dicionario = {1: 'IGTI', 2: 'Bootcamp', 3: 'IGTI'}
print('Dicionario com chave inteiras:')
print(dicionario)

# Criando um dicionario com varios tipos de chaves e valores
dicionario = {'escola': 'IGTI', 1: [1, 2, 3, 4]} # posso adicinar até mesmo uma lista
print('Dicionario com diferentes tipos de chaves e valores')
print(dicionario)

# Criando dicionarios coma palavra função Dict
dicionario = dict({1: 'IGTI', 2: 'Bootcamp', 3: 'IGTI'})
print('Criando dicionario com o metodo dict():')
print(dicionario)

# Criando dicionarios com estilo (chave,valor)
dicionario = dict([(1, 'IGTI'),(2, 'Bootcamp')]) # criando dicionario a partir de tuplas
print('Criando dicionario com par de chaves:')
print(dicionario)

# Criando dicionario vazio
dicionario[0] = 'IGTI'
dicionario[2] = 'Bootcamp'
dicionario[3] = 1
print('Adicionando elementos a um dicionario:')
print(dicionario)

# Realizando a atualização de um elemento em um dicionario.
dicionario[2] = 'MBA'
print('Atualizando o valor da chave [2] no dicionario:')
print(dicionario)

# Acessando elementos em um dicionario
# Criando um dicionario
dicionario = {'a': 'azul', 'v': 'verde', 'r': 'rosa'}
# Acessando um elemento através da chave
print('Acessando o elemento através da chave:')
print(dicionario['a'])

# Acessando um elemento através do metodo get()
print('Acessando através do metodo get():')
print(dicionario.get('v'))

#Removendo um elemento de um dicionario.
# Initial dicionary
dicionario = {1: 'IGTI', 2: 'Bootcamp', 3: 'MBA',
              'brasil': {'v': 'verde', 'a': 'azul', 'am': 'amarelo'},
              'minas': {'vm': 'vermelho', 'b': 'branca'}}
print('Dicionario inicial:')
print(dicionario)    

# Deletendo um valor pela chave.
del dicionario[3]
print('Deletendo um elemento pela chave:')
print(dicionario)



