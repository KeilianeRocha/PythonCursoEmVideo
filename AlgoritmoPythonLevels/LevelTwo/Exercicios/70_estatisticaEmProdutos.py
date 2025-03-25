# TODO: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# Qual é o total de gasto na compra.
# Quantos produtos custam mais de R$ 1000.
# Qual é o nome de produto mais barato.

from time import sleep

total = cont = totProdut = totMil = menorPreco = 0
barato = ' '

print(f"{'Pak n Save ':=^60}")

while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço R$ "))
    cont += 1
    totProdut += preco
    if preco > 1000:
        totMil += 1
    if cont == 1: # essa linha pode ser simplificada, mas ainda não tenho maturidade pra isso :p
        #obs: ela é uma repetição do if anterior e poderia usar um 'or' para simplificar
        menorPreco = preco
        barato = produto
    else:
        if preco < menorPreco:
            menorPreco = preco
            barato = produto
    opcao= ' '
    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if opcao == "N":
        print(" Calculando...")
        sleep(1)
        print(f"Total da compra foi → → → → → → → → → → → → R${totProdut:.2F}")
        print(f"Aquantidade de produtos custando R$ 1.000 foi de {totMil}")
        print(f"O produto mais barato foi {barato} que custa R${menorPreco:.2f}")
        
        break
print(f"{'Fim do Programa ':=^60}")
