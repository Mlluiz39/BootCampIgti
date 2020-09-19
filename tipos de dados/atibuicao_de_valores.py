# Atribuição de valores
# Identificador = Expressão

cateto_a = 4
endereco = id(cateto_a)
print(endereco)

hexa_endereco = hex(endereco) # endereço na posição de memoria em hexadecimal
print(hexa_endereco)

# Exemplo de como fica armazenada na memoria, ou seja fica no mesma posição se for atribuido o mesmo valor.

a = 10
print(a)
print(id(a))

b = 10
print(b)
print(id(b))

id(a) == id(b) # vai retornar como verdadeiro pois ficam na mesma posição

# Atribuindo valores e onde acontece o Garbage Collector
# Ou seja em python ele ocupa o espaço vazio da memoria
x = 1
endereco=id(x)
print(hex(endereco))

x = x+1
endereco = id(x)
print(hex(endereco))
