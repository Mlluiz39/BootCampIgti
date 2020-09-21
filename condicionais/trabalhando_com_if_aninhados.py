# If com condições mais elaboradas
# if com condicional or
altura = int(input('Entre com sua altura (em centimetros): '))
if (altura < 150) or (altura > 180):
    print('Você não pode brincar ')
else:
    print('Você pode brincar ')

# Adivinhando o resultado da divisão
numerador = float(input('Entre como numerador: '))
denominador = float(input('Entre com  denominador: '))

chute = float(input('Entre com seu chute para o resultado: '))

resultado = numerador / denominador

maior = abs(resultado)

# Verifica se o chute é até 1/10 do real
if abs((chute - resultado) / maior) <= 0.1:
    print('Seu chute está correto parabens !!')
else:
    print('Que pena o valor correto é {}'.format(resultado))

# if aninhados
i = 10
if (i == 10):
# primeiro if
    if (i < 15):    
        print('i é menor que 15')
# O if aninhado só é executado se o anterior for executado
    if (i < 12):
        print('i tambem é menor que 12')
    else:
        print('i é maior que 15')

print('continua o programa...')

x = float(input('Entre com o primeiro numero: '))
y = float(input('Entre com o segundo numero: '))

print('(1) + soma os dois numeros')
print('(2) - subtrai os dois numeros')
print('(3) * multiplica os dois numeros')
print('(4) / divide os dois numeros')

escolha = int(input('Escolha uma das opções: '))

if escolha == 1:
    print(x + y)
else:
    if (escolha == 2):
        print(x - y)
    else:
        if (escolha == 3):
            print(x * y)
        else:
            if (escolha == 4):
                print(x / y)
            else:
                print('Opção invalida')




