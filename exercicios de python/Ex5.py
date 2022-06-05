medida = float(input('Digite uma distância em metros:'))
cm  = medida * 100
mm = medida * 1000
km= medida / 1000
hm= medida / 100
dam= medida / 10
dm= medida * 10

print(f'A medida {medida}m correspode a {cm}cm')
print(f'A medida {medida}m correspode a {mm}mm')
print(f'A medida {medida}m correspode a {km}km')
print(f'A medida {medida}m correspode a {hm}hm')
print(f'A medida {medida}m correspode a {dam}dam')
print(f'A medida {medida}m correspode a {dm}dm')