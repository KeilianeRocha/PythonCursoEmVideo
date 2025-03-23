# TODO: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# Qual é o total de gasto na compra.
# Quantos produtos custam mais de R$ 1000.
# Qual é o nome de produto mais barato.

total = 0
cont = 0

produto = str(input("Nome do Produto: "))
preco = float(input("Preço R$ "))
opcao = str(input("Quer continaur? [S/N]")).strip().upper()

print("-" * 40)
print(f"Total da compra foi R${total:.2F}")
print(f"Temos {cont} produtos custando mais de R${total:.2F}")
print(f"O produto mais barato foi {produto} que custa R${preco:.2f}")


print(f"{'Fim do Programa ':=^30}")
