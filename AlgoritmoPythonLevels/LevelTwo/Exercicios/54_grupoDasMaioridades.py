# TODO: Crie um programa que leia o ano de nascimento de 7 pessoas no
# mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são maiores.

from datetime  import date


anoAtual = date.today().year
totMaior = 0
totMenor = 0
for pessoas in range(1, 8):
    nascAno = int(input(f"Em que ano a {pessoas}° Epessoa nasceu(AAAA)? "))
    idadeAtual = anoAtual - nascAno
    # print(idadeAtual)
    if idadeAtual >= 21:  #< == MAIOR
        totMaior += 1
    else:
        totMenor += 1

print(f"Ao todo tivemos {totMaior} pessoas MAIORES de idade")
print(f"Ao todo tivemos {totMenor} pessoas MENORES de idade")

print(f"{'Fim do Programa ':=^30}")
