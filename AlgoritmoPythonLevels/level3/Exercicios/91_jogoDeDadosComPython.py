# TODO: Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
# aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionario 
# em ordem, sabendo que o vecedor tirou o maior número no dado.


from operator import itemgetter  # Importa itemgetter para ordenar os jogadores 
# pelo valor do dado
from random import randint  # Importa randint para sortear números aleatórios 
# entre 1 e 6
from time import sleep  # Importa sleep para criar pausas entre as exibições 
# no terminal


jogador = {}  # Cria um dicionário vazio para armazenar os nomes dos jogadores 
# e os valores sorteados
for c in range(1, 5):  # Loop de 1 até 4 (inclusive) para representar os 4 
    #jogadores
    jogador[f"jogador {c}"] = randint(1, 6)  # Sorteia um número de 1 a 6 e 
    # associa ao jogador correspondente


ranking = list()  # Cria uma lista vazia para armazenar a ordem do ranking (não 
# necessária neste ponto ainda)
print("Valores sorteados:")
for k, v in jogador.items():  # Percorre o dicionário mostrando os valores sorteados
    print(f"{k} tirou {v} no dado")  # Mostra o nome do jogador e o valor que ele tirou
    sleep(1)  # Pausa de 1 segundo para deixar a exibição mais dinâmica

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print("-=" * 30)
print(" == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):  # Percorre o ranking ordenado com o índice da posição
    print(f"  {i+1}° lugar: {v[0]} com {v[1]}.")  # Exibe a posição, o nome do 
    # jogador e o valor que ele tirou
