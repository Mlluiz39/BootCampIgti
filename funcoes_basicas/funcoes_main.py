# Função main basica em python

def main():
    print('Ola Mundo!')

if __name__ == '__main__':
    main()

# Identificando o contexto em que estamos trabalhando
print('A variavel __name__ informa qual é o contexto em que estamos executando o arquivo.')
print('O valor da variavel __name__ é: ', repr(__name__))

# Importando o meu_programa_main.py
import meu_programa_main 

# Utilizando a função main para deixar o codigo "mais limpo"

from time import sleep


def process_data(data):
    print('Iniciando o procesamento de algum dado...')
    modifield_data = data + 'o dado foi modificado'
    sleep(3)
    print('Processamento de dado terminado')
    return modifield_data

def read_data_from_web():
    print('Lendo dados da web')
    data = 'Dados da web lidos'
    return data

def write_data_database(data):
    print('Armazenando dados em um database')
    print(data)

def main():
    data = read_data_from_web()
    modifield_data = process_data(data)
    write_data_database(modifield_data)

if __name__ == '__main__':
    main()