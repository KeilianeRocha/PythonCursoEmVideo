# TODO: Faça um programa que jogue par ou ímpar com o computador.
# o jogo so será interrompido quando o jogador PERDER,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.

from random import randint


vit = 0


print('-'*30)
print("Famos jogar um jogo")
print('-' *30)

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 11)  # Gera números aleatórios entre 0 e 10
    total = jogador + computador
    opcao = ' '
    while opcao not in 'PpIi':
        opcao = str(input("PAR ou ímpar [P/I]")).strip().upper()[0] #'[0] pega so a 1° letra
    print(f"Você jogou {jogador} e o computador jogou {computador}.\nTotal de {total}")
    print("DEU PAR" if total % 2 == 0 else "DEU")
    if opcao == 'P': 
        if total % 2 == 0:
            print("VOCÊ VENCEU!")
            vit += 1
        else:
            ("VOCÊ PERDEU!")
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print("VOCÊ VENCEU!")
            vit += 1
        else:
            print("VOCÊ PERDEU!")
            break
    print("Vamos jogar novamente?")
print(f"GAME OVER! Você venceu {vit} vezes.")
