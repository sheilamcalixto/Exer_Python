
frase = input('Digite uma frase:')

resultado = frase.replace('Olá', 'BOM DIA')
resultado2 = frase.upper()
resultado3 = frase.lower()
resultado4 = frase.isupper()
resultado5 = frase.capitalize()
resultado6 = frase.title()
resultado7 = frase.strip()
resultado8 = frase.split()
resultado9 = '-'.join(frase)
resultado10 = frase.count('o')
resultado11 = len(frase)

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print(resultado9)
print(resultado10)
print(resultado11)
print('Olá' in frase)