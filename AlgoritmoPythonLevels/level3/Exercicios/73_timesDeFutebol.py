# TODO: Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato
# brasileiro de futebol, na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados.
# Os ultimos 4 colocados da tabela
# Uma lista com os times em ordem alfabética.
# Em que posição na tabela esta o time da Chapecoense.

# ✅ Cabeçalho centralizado e formatado com 100 caracteres de largura
print(f"{'TABELA CAMPEONATO BRASILEIRO ':=^100}")

# ✅ Tupla com times (imutável)
lista = (
    "Corinthias",
    "Palmeiras",
    "Santos",
    "Grêmio",
    "Curitiba",
    "Avaí",
    "Ponte Preta",
    "Atrético-Go",
)

# Loop infinito desnecessário (executa apenas uma vez devido ao break)
while True:
    # Mostra os 5 primeiros times (slice [0:5])
    print(f"Os 5 primeiros são {lista[0:5]}")

    # Mostra os times a partir do 5° (slice [4:])
    print(f"Os 4 últimos são {lista[4:]}")

    # Mostra times em ordem alfabética (sorted cria nova lista ordenada)
    print("Times em ordem alfabética:", sorted(lista))

    # Problema grave: sobrescreve a variável 'lista' no loop for
    for posicao, lista in enumerate(lista):
        if lista == "Santos":
            # Mostra posição do Santos (ajustada para começar em 1°)
            print(f"O Santos esta na {posicao + 1}° na posição")

    # Break encerra o loop while imediatamente (tornando-o redundante)
    break
