print('---PROGRAMA QUE APRESENTE O SENO,COSSENO E TANGÊNTE DE UM ÂNGULO---')

import math

angulo = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a TANGÊNTE de {:.2f}'.format(angulo, tan))
