# TODO: Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um numero entre 0 e 10.
# So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
from time import sleep

totTentativas = 0
palpites = 0
acertou = False

computador = randint(0, 10) #Gera números aleatórios entre 0 e 10 
print(f"{' Jogo da advinhação ':=^30}")

while not acertou: # Enquanto não acertar
  
    print('='*60)
    jogador = int(input("Em que número eu pensei? "))
    palpites += 1 #Contagem de palpites
    print("PROCESSANDO...")
    sleep(1) # Computador espera para seguir
    if jogador == computador: 
        acertou = True
    else:
        if jogador < computador:
            print("Mais! Tente novamente...")
        elif jogador > computador:
            print("Menos! Tente novamente...")

print("Parabéns! Você venceu!")
print(f"Total de tentativas: {palpites}")
print(f"{' Fim do Programa ':=^30}")
