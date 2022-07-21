l = float(input('Lagura da parede em Metros: '))
a = float(input('Altura da parede em Metros: '))

area = float(l*a)
litroTinta = area*0.5

print('-------------')
print('Area: {}m²'.format(area))
print('Será necessario {} Litros de tinha para pintar essa área'.format(litroTinta))
