preco = float(input('Qual é o prço do produto? R$ '))
desconto = (preco * 5 / 100)
novo = preco - desconto



print(f'O produto que custava R${preco}, na promoção com deconto de 5% vai custar R${novo :.2f}')