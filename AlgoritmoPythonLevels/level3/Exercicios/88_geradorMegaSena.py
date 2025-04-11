# TODO: Faca um programa que ajude um jogador da mega sena a criar palpites. O programa
# vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
# cada jogo, cadastrando tudo em uma lista composta. (1 a 60)

# Importa as bibliotecas necessárias
from time import sleep
from random import randint

# Inicializa listas vazias
lista = list()
jogos = list()

# Exibe cabeçalho decorativo
print("-" * 35)
print(f"{' GERADOR DE NÚMEROS DA MEGA SENA ':=^30}")
print("-" * 35)

# Solicita a quantidade de jogos ao usuário
quant = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1

# Loop para gerar a quantidade solicitada de jogos
while tot <= quant:
    cont = 0

    # Loop para sortear 6 números únicos entre 1 e 60
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    # Ordena a lista e adiciona aos jogos
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

# Exibe os jogos sorteados
print("-=" * 3, f"SORTEANDO {quant} JOGOS", "-=" * 3)
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: Os números sorteados foram {l}")
    sleep(1)

# Exibe mensagem final
print(f"{' BOA SORTE!':=^30}")
