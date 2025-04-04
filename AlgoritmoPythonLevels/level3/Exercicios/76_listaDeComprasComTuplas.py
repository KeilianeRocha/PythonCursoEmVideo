# TODO: Crie um programa que tenha uma tupla única com nomes de produtos e seus preços,
# na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.



# Tupla com produtos e preços intercalados
produtos = ("Arroz", 25.0, " Feijão", 12.0, "Carne", 45.0)

# Cabeçalho decorado
print("-" * 40)
print(f"{'LISTA DE COMPRAS':=^40}")  # Título centralizado com preenchimento
print("-" * 40)

# Loop problemático: está usando posição fixa [0] em todos os pares
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        # Sempre imprime produtos[0] ("Arroz") em vez do produto atual
        print(f"{produtos[0]:.<30}", end="")  # Alinhado à esquerda com pontos
    else:
        # Formatação correta do preço (alinhado à direita)
        print(f"R${produtos[pos]:>7.2f}")

print("-" * 40)  # Rodapé decorativo
