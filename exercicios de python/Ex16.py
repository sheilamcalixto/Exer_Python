### Dado três números inteiros positivos. Diga se é primo, par,ímpa e qual o número sucessor.
import math

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o terceiro número: '))

resultado1 = n1 % 1
resultado2 = n1 % 1
resultado3 = n1 % 1
resultado4 = n1 % 1

print(f'Resultado {resultado1} ')
print(f'Resultado {resultado2} ')
print(f'Resultado {resultado3} ')
print(f'Resultado {resultado4} ')


if resultado1 == 0:
    resultado1 = 'É um número primo e é um número par'

elif resultado1 != 0:
    resultado1 = 'Não é um número primo e éum número ímpar'

if resultado2 == 0:
    resultado2 = 'É um número primo e é um número par'

elif resultado2 != 0:
    resultado2 = 'Não é um número primo e é um número ímpar'

if resultado3 == 0:
    resultado3 = 'É um número primo e é um número par'

elif resultado3 != 0:
      resultado3 = 'Não É um número primo e é um número ímpar'

if resultado4 == 0:
    resultado4 = 'É um número primo e é um número par'

elif resultado4 != 0:
      resultado4 = 'Não é um número primo e não é um número par'


print('---------------------------------------')
print(f'Resultado {resultado1} ')
print(f'O sucessor do número {n1} é: {n1 + 1}')
print('---------------------------------------')
print(f'Resultado {resultado2}')
print(f'O sucessor do número {n2} é: {n2 + 1}')
print('---------------------------------------')
print(f'Resultado {resultado3}')
print(f'O sucessor do número {n3} é: {n3 + 1}')
print('---------------------------------------')
print(f'Resultado {resultado4}')
print(f'O sucessor do número {n4} é: {n4 + 1}')
print('---------------------------------------')
