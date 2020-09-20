# Funcionamento do condicional if
# O caso do if
# Exemplo
print('Execução antes do if...')
numero = float(input('Entre com um numero: '))
if numero %2 == 0:
    print('Esse é um numero par.')

print('Execução apos o if...')

print('Execução antes do if...')
numero = float(input('Entre com um numero: '))
if numero > 0:
    print('Esse numero é positivo: ')

print('Execução apos o if...')    

i = 10
if (i > 15):
    print('10 é maior que 15')

print('Continuando o programa...')   

# Exemplo com else
print('Execução antes do if...')

numero = float(input('Entre com um numero: '))
if numero %2 == 0:
    print('Esse numero é par. \n')
else:
    print('Esse é um numro impar. \n')

print('Execução apos o if...')

i = 20
if (i < 15):
    print('i é menor que 15')
    print('Execução do if...')
else:
    print('i é maior que 15')
    print('Executando o else...')

print('Continuando o programa...')

# Encontrando o maior valor entre dois numeros inteiros digitados
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
if (x > y):
    print(' O primeiro valor (%2d) é maior que o segundo valor(%2d)'%(x, y))
else:
    print(' O primeiro valor (%2d) é menor que o segundo valor(%2d)'%(x, y))

