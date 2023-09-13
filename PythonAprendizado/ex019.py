print('---PROGRAMA QUE SORTEIE UM ALUNO, DENTRE 4---')

import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

nome = [aluno1, aluno2, aluno3, aluno4]
nomeEscolhido = random.choice(nome)

print('O nome escolhido foi: {}'.format(nomeEscolhido))
