# TODO: Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato
# brasileiro de futebol, na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados.
# Os ultimos 4 colocados da tabela
# Uma lista com os times em ordem alfabética.
# Em que posição na tabela esta o time da Chapecoense.


print(f"{'TABELA CAMPEONATO BRASILEIRO ':=^100}")

lista = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 'Curitiba', 'Avaí', 'Ponte Preta', 'Atrético-Go')
while True:
    print(f"Os 5 primeiros são {lista[0:5]}")
    print(f"Os 4 últimos são {lista[4:]}")
    print("Times em ordem alfabética:",sorted(lista))
    for posicao, lista in enumerate(lista):
        if lista == 'Santos':
            print(f"O Santos esta na {posicao + 1}° na posição")
    break


# FIXME: Corrigir cod.
