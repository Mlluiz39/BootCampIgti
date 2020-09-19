# Criando uma lista em python
# Mutáveis
#Ordenadas
# Começa com indice [0]
lista = []
print('lista vazia: ')
print(lista)
print(type(lista))

#Lista com string.
lista = ['IGTI']
print('Lista com string: ')
print(lista)

#Lista com varios valores.
lista = ['IGTI', 'MBA', 'Python']
print('Lista com varias strings: ')
print(lista[0])
print(lista[2])

# Criando lista de listas.
lista = [['IGTI', 'MBA'], ['Python']]
print('Lista com varias dimensões: ')
print(lista)

# Criando uma lista com tipos diferentes de dados.
lista = [['IGTI', 'MBA'], 123, 'Python']
print('Lista com varios dimensões e valores: ')
print(lista)

# Adcionando elementos em uma lista
#Adcionando elemento com append que sempre vai ao final da lista.
lista = [1, 2, 3, 4]
print('Lista numerica: ', lista)
lista.append(5)
print('Lista numerica adicionada um numero: ', lista)
lista2 = [1, 2, 3]
print('Lista numerica: ', lista2)
lista2.append('IGTI')
print('Lista numerica adicionada uma string: ', lista2)

# Adicionando elementos com insert que por sua vez coloca em uma possição selecionada.
lista3 = ['azul', 'verde', 'vermelho', 'amarelo']
print(lista3)
lista3.insert(2, 'preto')
lista3.insert(0, 'rosa')
print(lista3)
 
 # Adicionando elementos com extend a difrença entre ele e o append e que ele coloca varios valores.
lista3.extend(['branco','cinza',123, 5.0, 7j,]) 
print('lista apos aplicar operação extend: ')
print(lista3)

# Acessando elementos de uma lista
lista = ['azul', 'verde', 'vermelho', 'amarelo']
print('Acessando elementos na lista: ')
print(lista[0])
print(lista[2])

# Acesando elementos nomsentido contrario.
print('Acessando elementos no sentido contrario: ')
# Ultimo elemento da lista.
print(lista[-1])
# Penultimo elemento da lista.
print(lista[-2])

# Acessando valores em uma lista. aninhadas.
lista = ['Azul', 'verde', 'vermelho', 'amarelo', [100, 200, 300, 400]] # os valores interiros estão dentro de uma lista é posição '4'
# Acessando o elemento "200" da lista
print('Acessando elemento da lista aninhada: ')
print(lista[4][1]) 

# Criando e removendo elementos de uma lista
lista_rem = [1, 2, 3, 4, 5, 6, 
             7, 8, 9, 10, 11, 12,
             'Azul', 'verde', 35, 'amarelo']
print('lista inicial: ')
print(lista_rem)
# Lista apos a remoção
lista_rem.remove(5)
lista_rem.remove('verde')
print('Lista com objetos removidos: ')
print(lista_rem)

# Removendo elementos com o pop que por sinal remove o ultimo elemento caso não seja apontado.
lista_rem.pop()
print('lista após utilizar o pop()')
print(lista_rem)

# Removendo elemento com pop porem apontando a posição.
lista_rem.pop(10) # este numero entre parenteses corresponde a posição de remoção.
print('lista apos remover um elemento especifico com pop:')
print(lista_rem)



          


