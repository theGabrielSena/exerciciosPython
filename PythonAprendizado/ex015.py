print('---PROGRAMA QUE FAÇA GESTÃO DE ALUGUEL DE CARROS---')

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

soma = (dias*60) + (km*0.15)

input('O total a pagar é de: {:.2f}'.format(soma))
