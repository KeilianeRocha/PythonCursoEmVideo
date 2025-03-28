# TODO: Crie um programa que tenha uma tupla única com nomes de produtos e seus preços,
# na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""
Listagem de preços
produtos .......... R$ preços.....
"""

produtos = ('Arroz', 25.0,' Feijão', 12.0, 'Carne', 45.0)
print('-' * 40)
print(f"{'LISTA DE COMPRAS':=^40}")
print("-" * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[0]:.<30}", end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print("-" * 40)
