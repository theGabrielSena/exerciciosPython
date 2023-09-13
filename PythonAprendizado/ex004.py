print('---PROGRAMA QUE APRESENTA TODOS OS DETALHES DE ALGO DIGITADO---')

algo = input('Digite qualquer coisa: ')

print('O tipo primitivo é: {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está escrito em letras maiúsculas? {}'.format(algo.isupper()))
print('Está escrito em letras minúsculas? {}'.format(algo.islower()))
