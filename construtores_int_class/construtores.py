 # Criando uma classe Carro

class Carro:
    def __init__(self, numero_portas, preco):  # Construtor da classe
        self.numero_portas = numero_portas
        self.preco = preco
        print('Objeto carro instanciado com sucesso')
    def get_numero_portas(self):
        return self.numero_portas


carro_1 = Carro(4, 50000)

portas_carro_1 = carro_1.get_numero_portas()
print(' Meu carro possui %d portas.' %portas_carro_1)

# Novo objeto sendo chamado

carro_2 = Carro(2, 80000)
portas_carro_2 = carro_2.get_numero_portas()
print(' Meu carro possui %d portas.' %portas_carro_2)

print('Endereço de memória carro_1: ', hex(id(carro_1))) # Endereço de memória "0x7f2a170c6040"
print('Endereço de memória carro_2: ', hex(id(carro_2))) # Endereço de memória "0x7f2a1708f940"

# Podemos ter mais de um construtor para uma classe

string = str(6)
print(string)
inteiro = int('6')
print(inteiro)
float_1 = float('6')  # construtor recebendo uma string
print(float_1)
float_2 = float(inteiro) # construtor recebendo um inteiro
print(float_2)
lista = list('a b c') # em uma lista ele imprime até os espaços em branco
print(lista)

# Métodos acessores e modificadores
# Getters (Método Acessores)
# Setters (Métodos Modificadores)

# Importando modulo array
import array as ar

# Inicializando o array
meu_array = ar.array('i', [5, 1, 3, 4, 2, 2, 7])

# print do array
print(meu_array)

# Acessando o indice do valor igual a 2
print(meu_array.index(2))

# Acessando a quantidade de valores 2 existentes
print(meu_array.count(2))

# Criando uma classe carro
class Carro:
    def __init__(self, numero_portas, preco):
        self.numero_portas = numero_portas
        self.preco = preco
        print('Objeto carro instanciado com sucesso')
    def get_numero_portas(self):
        return self.numero_portas
    def set_numero_portas(self, novo_numero_portas):
        self.numero_portas = novo_numero_portas


carro_3 = Carro(4, 50000)
print(' Numero de portas antes:', carro_3.get_numero_portas())  # metódo get - não modifica o estado do objeto
carro_3.set_numero_portas(2)  # metódo set modifica o estado do objetos
print(' Novo numero de portas:', carro_3.get_numero_portas())

# "Cria uma referencia ao objeto carro"    / nesse codigo está claro que devemos tomar cuidado, 
# pq ao setar qualquer um dos objetos eles ficaram com o mesmo valor \

carro_4 = carro_3        # Aqui coloquei para que ficasse igual ao carro_3
print('Numero de portas do carro_4:', carro_4.get_numero_portas())

# Modifica o numero de portas do carro_4
carro_4.set_numero_portas(3)
print('Novo numero de portas do carro_4:', carro_4.get_numero_portas())

# Numero de portas do carro_3
print('Numero de portas do carro_3:', carro_3.get_numero_portas())


# Classes que não possuem métodos mutaveis - int, float, string
string = 'Estou estudando Python'
print(id(string))
string = string + ' ''no IGTI'
print(id(string))
print(string)










