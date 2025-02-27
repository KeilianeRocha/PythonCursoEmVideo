# TODO: Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

"""
while True:
    computador = randint(0, 5)
    print(f"{' Jogo da advinhação ':=^30}")
    print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
    print('='*60)
    jogador = int(input("Em que número eu pensei? "))
    print("PROCESSANDO...")
    sleep(3) # COMPUTADOR ESPERA PARA SEGUIR 
    if jogador == computador:
        print("Parabéns! Você venceu!")
        break
    else:
        print(f"Você perdeu eu pensei no número {computador} e não no número {jogador}! Tente outra vez")
print(f"{' Fim do Programa ':=^30}")
"""

#CÓDIGO MELHORADO

# Constantes
INTERVALO_MIN = 0
INTERVALO_MAX = 5
TEMPO_ESPERA = 3


def exibir_cabecalho():
    """Exibe o cabeçalho do jogo."""
    print(f"{' Jogo da Advinhação ':=^30}")
    print(
        f"Vou pensar em um número entre {INTERVALO_MIN} e {INTERVALO_MAX}. Tente adivinhar..."
    )
    print("=" * 60)


def obter_palpite_jogador():
    """Obtém e valida o palpite do jogador."""
    while True:
        try:
            palpite = int(
                input(f"Em que número eu pensei? ({INTERVALO_MIN}-{INTERVALO_MAX}): ")
            )
            if INTERVALO_MIN <= palpite <= INTERVALO_MAX:
                return palpite
            else:
                print(
                    f"Por favor, insira um número entre {INTERVALO_MIN} e {INTERVALO_MAX}."
                )
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


def jogar():
    """Função principal que executa o jogo."""
    while True:
        exibir_cabecalho()
        numero_pensado = randint(INTERVALO_MIN, INTERVALO_MAX)
        palpite_jogador = obter_palpite_jogador()

        print("PROCESSANDO...")
        sleep(TEMPO_ESPERA)

        if palpite_jogador == numero_pensado:
            print("Parabéns! Você venceu!")
            break
        else:
            print(
                f"Você perdeu! Eu pensei no número {numero_pensado} e não no número {palpite_jogador}. Tente outra vez."
            )

    print(f"{' Fim do Programa ':=^30}")


# Inicia o jogo
jogar()
