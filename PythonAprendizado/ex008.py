print('---PROGRAMA QUE RECEBE METROS E CONVERTE PARA CENTÍMETROS E MILÍMETROS---')

metros = float(input('Digite quantos metros deseja converter: '))

print('Quilômetros: {:.3f}\n'
      'Hectômetros: {:.2f}\n'
      'Decâmetros: {:.1f}\n'
      'Decímetros: {:.2f}\n'
      'Centímetros: {:.2f}\n'
      'Milímetros: {:.2f}'
      .format(metros/1000, metros/100, metros/10, metros*10, metros*100, metros*1000)
      )
