# TODO: Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um numero entre 0 e 10.
# So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
from time import sleep

totTentativas = 0

print(f"{' Jogo da advinhação ':=^30}")

while True:
    computador = randint(0, 10)
    print('='*60)
    jogador = int(input("Em que número eu pensei? "))
    print("PROCESSANDO...")
    sleep(1) # COMPUTADOR ESPERA PARA SEGUIR 
    if jogador <= computador: 
        print("Mais! Tente novamente...")
        if jogador >= computador:
            print("Menos! Tente novamente...")
    else:
        if computador <= jogador:
            print("Mais! Tente novamente...")
        elif computador >= jogador:
            print("Menos! Tente novamente...")
        else:
           if jogador == computador:
            print("Parabéns! Você venceu!")
        break
print(f"{' Fim do Programa ':=^30}")
