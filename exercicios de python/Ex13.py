import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ânggulo {angulo} tem o SENO de {seno :.2f}')
print(f'O ângulo {angulo} tem o COSSENO de {cosseno :.2f}')
print(f'O Ângulo {angulo} tem a TANGENTE de {tangente :.2f}')
