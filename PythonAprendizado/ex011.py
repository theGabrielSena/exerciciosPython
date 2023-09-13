print('---PROGRAMA CÁLCULO DE ÁREA DE UM MURO---')

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura*altura

litroTinta = 2

litroTinta = area/litroTinta

print('O cálculo de área foi de {}m²\nSerá necessário {} litros de tinta'.format(area, litroTinta))
