# TODO: Faça um programa que jogue par ou ímpar com o computador.
# o jogo so será interrompido quando o jogador PERDER,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.

from random import randint

par = 0
impar = 0
computador = 0
cont = 0

print('-'*30)
print("Famos jogar um jogo")
print('-' *30)
jogador = int(input("Diga um valor: "))
opão = str(input("PAR ou ímpar [P/I]")).strip().upper()
computador = randint(0, 10)  # Gera números aleatórios entre 0 e 10


print(f"Você jogou {jogador} e o computador jogou {computador}.\nTotal de {cont} Deu PAR")
print(f"Você jogou {jogador} e o computador jogou {computador}.\nTotal de {cont} Deu ÍMPAR")

print("VOCÊ VENCEU!")
print("VOCÊ PERDEU!")

print("GAME OVER! Você venceu {} vezes.")

computador = randint(0, 10)  # Gera números aleatórios entre 0 e 10
