print('---PROGRAMA CONVERSÃO DE CAMBIO---')

dolar = 4.9828
real = float(input('Digite o valor que você possui em R$: '))

print('Você pode comprar ${:.2f} dólares'.format(real/dolar))
