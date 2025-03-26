# TODO: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pduto = float(input('Qual o preço do produto? R$'))
desc = pduto - (pduto * 5/100)
print(f"O produto que custava R${pduto:.2f}, na promoção com desconto de 5% vai custar R${desc:.2f}")
#print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(pduto, desc))

