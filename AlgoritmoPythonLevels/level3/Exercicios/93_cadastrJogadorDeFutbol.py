# TODO: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será quardado em um dicionario, incluindo o total de gols feitos durante o campeonato.

jogador = dict()  # Cria um dicionário para armazenar os dados do jogador
partidas = list()  # Lista para guardar os gols de cada partida


jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Loop para registrar a quantidade de gols em cada partida
for c in range(0, tot):
    partidas.append(int(input(f"  Quantos gols na partida {c}? ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print("-=" * 30)

# Exibe cada chave (campo) e valor do dicionário
for k, v in jogador.items():
    print(f" O campom {k} tem o valor {v}")
print("-=" * 30)

# Mostra quantas partidas o jogador jogou (baseado no tamanho da lista de gols)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")

# Exibe os gols feitos em cada partida
for i, v in enumerate(jogador['gols']):
    print(f" → Na partida {i+1}, fez {v} gols.")

# Mostra o total de gols no final
print(f"Totalizando {jogador['total']} gols.")
