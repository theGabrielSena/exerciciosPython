from math import sqrt
from emoji import emojize

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

print(emojize('Olá, Mundo! :globe_showing_Americas:', language='alias'))
