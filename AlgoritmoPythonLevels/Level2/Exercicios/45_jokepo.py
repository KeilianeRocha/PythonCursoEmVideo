# TODO: Crie um programa que faça o computador jogar jokenpô com você.
# usando módulos e condicionais aninhadas

from time import sleep
from random import randint

TEMPO_ESPERA = 1
jogador = 0

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("_-_" * 9)
print(f"O computador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")
print("_-_" * 9)
print(
    """Suas opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA 
"""
)
print("_" * 20)
jogador = int(input("Qual a sua jogada? "))
print("_" * 20)
print("JO")
sleep(TEMPO_ESPERA)
print("KE")
sleep(TEMPO_ESPERA)
print("PO!!!")
sleep(TEMPO_ESPERA)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada inválida!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada inválida!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada inválida!")
print(f"{'Fim do Programa ':=^30}")
