# tipos de argumentos em python
# 1- Default Arguments
# 2- Keyword Arguments
# 3- Artitrary Arguments
# Exemplo de função

def concatena_nome_mensagem(nome, mensagem): # a função possue dois parametros
    """

    @type nome: parametro da função
    """
    print('Ola,', nome + '!'  + mensagem)
    # chamando a função corretamente

concatena_nome_mensagem('Maria', 'Bom dia')

# Exemplo de paramentro default

def concatena_nome_mensagem(nome, mensagem= 'Boa Noite !'): # a função possue dois parametros um como default
    print('Ola,', nome + '!'  + mensagem)

concatena_nome_mensagem('Maria') # Caso não seja setado na chamada ele pega a do
                                  #parametro da acima função

'''concatena_nome_mensagem('Maria', 'Bom descanso') neste caso ele altera o do default por este parametro (bom descanso)'''
 
 # Argumentos arbitrarios
# com *args olha eu não sei a quantidade de argumentos
# com **Rwargs olha não sei quantas variaveis vai ter

def print_nomes_dos_usuarios(*nomes): 
     for nome in nomes:
         print('Ola ' + nome + '! Bom Dia !')
          
        
print_nomes_dos_usuarios('Marcelo', 'Julia', 'Cilene')

def minha_funcao(**Kwargs):
    print(str(Kwargs))

minha_funcao(a=2, b='abc')

 #definição com a posição e apenas 2 valores

def somatoria(a, b):
    print('Somatoria é:', a + b)

somatoria(21, 5)

# definindo com *Args

def somatoria(*Args):
    total = 0
    for Arg in Args:
        total += Arg
    print('Somaroria é:', total)

somatoria(5, 10, 2)

        
 

