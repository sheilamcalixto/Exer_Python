largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

area = largura * altura
tinta = area / 2

print(f' Sua parede tem a dimensão de {largura}x{altura}m² e sua área é de {area}m².\n para pintar essa parede voce vai precisar de {tinta} litros de tinta.')
