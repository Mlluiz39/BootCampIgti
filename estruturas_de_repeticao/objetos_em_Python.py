s = 'Como vai você?'
print(type(s))
# referencia_ao_objeto.metodo(argumentos)
s = 'COMO VAI VOCÊ'
nova_string = s.lower()
print(nova_string)
# help(str) # aparece todas as opções 

# Operadores com string - metodos implicitos

s = input('Entre com seu nome: ')
t = input('Entre com onome da sua mãe: ')
if s <= t:
    print('Seu nome vem antes do que o da sua mãe.')
else:
    print('Seu nome vem depois do que o da sua mãe.')

# Lista
s = input('Entre com seu nome: ')
t = input('Entre com onome da sua mãe: ')
if s.__le__(t):
    print('Seu nome vem antes do que o da sua mãe.')
else:
    print('Seu nome vem depois do que o da sua mãe.')


