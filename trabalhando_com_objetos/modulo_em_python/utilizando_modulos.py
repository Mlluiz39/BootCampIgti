# Utilizando modulos em python

import math

print('O valor de pi é: ', math.pi) # sem formatação de duas casas
print('O seno de 45 é: %.2f '%(math.sin(math.pi/4))) # com formatação de duas casas usando f' string
print('O cosseno de 180 é: ', math.cos(math.pi))

import math,datetime

print(datetime.datetime.now())

# Utilizando modulos "build-in" em python

print('Modulo string: ', str(124))
print('Modulo float: ', float(123/12))

# modulo utilizado para monitorar a plataforma (S.O) que estamos utilizando

import platform

x = platform
plataforma = x.system()
print(plataforma)
print(x.processor)
print(x.python_version())

# Utilizar nossos proprios modulos

'''import meu_modulo

meu_modulo.boas_vindas('Marcelo')'''

# Carregando determinada rotina de um modulo

from math import factorial  # se usarmos o * importa tudo tbm  ex: "from math import *"

numero = 6
print('O fatorial de {} é {}'.format(numero, factorial(numero)))

# Modulos com apelidos

from math import factorial as ft

numero = 5
print('O fatorial de {} é {}'.format(numero, ft(numero)))


