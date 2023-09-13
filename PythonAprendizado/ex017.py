print('---PROGRAMA QUE CALCULE A HIPOTENUSA---')

from math import hypot

catetoOp = float(input('Digite o valor do cateto oposto: '))
catetoAdj = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(catetoOp, catetoAdj)

print('Esse triângulo possui um cateto oposto de {}, adjacente de {},'
      'formando a hipotenusa de {:.2f}'.format(catetoOp, catetoAdj, hipotenusa)
      )
