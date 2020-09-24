# Pontos a serem obs: na contrução de funções
# 1. qual nome da função: deve fazer sentido ao codigo, deve mostrar o que a função faz
# 2. Quais argumentos a função deve receber: Devemos definir quais os valores devem ser passados.
# 3. O que a função deve fazer: Devemos definir o papel da função em nosso programa
# 4. O que a função deve retornar: Apos realizar o processamento, qual o valor esperado

### Escreva uma função que retorne o valor absoluto de um numero ###

# 1- O nome da função será: valor_absoluto
# 2- A função vai receber um numero (inteiro ou float)
# 3- A função deve calcular o valor absoluto de um numero passado
# 4- A função deve retornar o valor absoluto
def valor_absoluto(num):
    '''Esta função retorna o valor absoluto de um numero'''

    if num >= 0:
        return num
    else:
        return -num

print(valor_absoluto(20))
print(valor_absoluto(-4.5))

### Escopo de um codigo em python

#Seja está função

def minha_funcao():            # Não recebe argumentos
    variavel_interna = 300     # Variavel definida no escopo da função
    print(variavel_interna)

minha_funcao()

# Acessando a variavel dentro de outra função

def minha_funcao():
    variavel_interna = 300   # Variavel interna da minha_função
    def minha_funcao_interna():  # função interna da função "minha_função"   # função aninhada
        print(variavel_interna)
    minha_funcao_interna()       # chamando a função interna dentro da função

minha_funcao()


# Escopo global

variavel_externa = 600  # variavel fora do escopo interno ou seja escopo global

def minha_funcao():
    print(variavel_externa)

minha_funcao()

print(variavel_externa)

# Modificando variaveis globais

variavel = 500   # escopo global (objeto diferente mesmo tendo o mesmo nome)

def  minha_funcao():
    variavel = 250  # mesmo tendo o mesmo nome representa objetos diferentes
    print(variavel)

minha_funcao()

print(variavel)

# Utilizando a palavra global

def minha_funcao():
    global variavel_global  # utiliza a palavra-chave global para definir uma variavel global no escopo da função
    variavel_global = 900

minha_funcao()

print(variavel_global)

# trocando o valor da variavel global dentro da função altera o valor da variavel

x = 700 # valor do objeto antes da palavra chave ser inserida no escopo da função

def minha_funcao():
    global x
    x = 350  # quando foi utilizado a plavra-chave a variavel interna se
    # tornou global, podendo assim ser alterado em qualquer parte do codigo
minha_funcao()

print(x)


