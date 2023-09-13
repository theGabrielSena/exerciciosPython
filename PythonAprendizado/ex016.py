print('---PROGRAMA QUE ARREDONDE O NÚMERO---')

from math import trunc

numero = float(input('Digite um número qualquer: '))
numero = trunc(numero)

print('O número arredondado: {}'.format(numero))
