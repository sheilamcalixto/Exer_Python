salario = float(input('Qaul é o salário do funcionário? R$ '))

novo_salario = salario + (salario*15/100)

print(f'Um funcionário que ganhava R${salario :.2f}, com 15% de aumento, passa a receber R${novo_salario :.2f}')