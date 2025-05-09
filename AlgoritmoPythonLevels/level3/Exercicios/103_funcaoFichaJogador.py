# TODO: Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostar a ficha do jogador, mesmo que algum dado
# não tenha sido informado corretamente.


def ficha(nomeJogador='<Desconhecido>', TotGols=0):
    print(f"O jogador {nomeJogador} fez {TotGols} gol(s) no Campeonato")



# Programa principal
nome = str(input("Nome do jogador: ")).title()
gol = str(input(f"Número de Gol(s) do Jogador: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(TotGols=gol)
else:
    ficha(nome, gol)

