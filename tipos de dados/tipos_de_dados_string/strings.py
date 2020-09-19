# Criando uma string
string = 'fundamentos de python no IGTI'
print('String com aspas simples')
print(string)
print(type(string))

# String com aspas duplas
string1 = "fundamentos de python no IGTI"
print("string com aspas duplas")
print(string1)
print(type(string1))

# String com aspas triplas
string2 = '''fundamentos de python no IGTI'''
print('''string com aspas triplas''')
print(type(string2))

# Aspas triplas em multiplas linhas
string3 = '''fundamentos de python
             do
             IGTI'''               # Ou seja consigo fazer quebra de linhas usando aspas triplas.
print('''string com multiplas linhas: ''')
print(string3)  

# Acessando elementos de uma string
# I N S T I T U T O I  G  T I
# 0 1 2 3 4 5 6 7 8 9 10 11 12
#-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3- 2- 1

string = 'institutoIGTI'
print('string: ')
print(string)

# Print do primeiro caracter 
print('O primeiro caracter da string é: ')
print(string[0])
print(string[-1])

# Tentando fazer update ou remove de uma string

#print("Caracter de posição 2: ",string[2])
#string[2] = "p"
#print("Realizando o update de um caracter da string: ")
#print(string) # vai dar erro pois as estrings uma vez definida ela se torna imutavel.

# Utilizando mais de um tipo de aspas em uma string
string1 = '''O IGTI possui "bootcamp" e 'MBA' em TI'''
print("string inicial com aspas triplas: ")
print(string1)

#Convertendo string em numero e vice versa
n_inteiro = 100
print(type(n_inteiro))
string_n_inteiro = str(n_inteiro)
print(string_n_inteiro)
print(type(string_n_inteiro))

string_n = "100"
print(type(string_n))
string_em_int = int(string_n)
print(string_em_int)
print(type(string_em_int))
