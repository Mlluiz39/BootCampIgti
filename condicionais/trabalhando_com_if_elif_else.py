i = 10
if (i == 10):
    print('i é igual a 10')
elif (i == 15):
    print('i é igual a 15')
elif (i == 20):
    print('i é igual a 20')
else:
    print('i não está nas condições')

####################################################################################################################

x = float(input('Entre com o primeiro numero: '))
y = float(input('Entre com o segundo numero: '))

print('(1) + soma os dois numeros')
print('(2) - subtrai os dois numeros')
print('(3) * multiplica os dois numeros')
print('(4) / divide os dois numeros')

escolha = int(input('Escolha uma das opções: '))

print('O resultado é: ', end='')

if escolha == 1:
    print(x + y)
elif (escolha == 2):
    print(x - y)
elif ( escolha == 3):
    print(x * y)
elif (escolha == 4):
    print(x / y)
else:
    print('Opção inválida !')

##################################################################################################################

x = int(input('Entre com o primeiro numero inteiro: '))
y = int(input('Entre com o segundo numero inteiro: '))
z = int(input('Entre com o terceiro numero inteiro: '))
if y > x:
    if z > y:
        print(z, 'é o maior numero.')
    else:
        print(y, 'é o maior numero')
else:
    if z > x:
        print(z, 'é o maior numero.')
    else:
        print(x, 'é o maior numero.')
print('fim do programa...')

###################################################################################################################

#Forma mais inteligente
x = int(input('Entre com o primeiro numero inteiro: '))
y = int(input('Entre com o segundo numero inteiro: '))
z = int(input('Entre com o terceiro numero inteiro: '))
#Primeiro chute
maior_numero = x
if y > maior_numero:
#ajusta o primeiro chute
    maior_numero = y
if z > maior_numero:
#ajusta o segundo chute
    maior_numero = z
print(maior_numero, 'é o maior numero.')
print('fim do programa...')

    