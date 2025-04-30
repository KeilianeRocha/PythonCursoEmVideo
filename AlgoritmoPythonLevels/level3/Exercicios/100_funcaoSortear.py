# TODO: Faça um programa que tenha uma lista chamada numeros e duas funções
# chamadas sorteia() e soma(). A primeira função vai sortear 5 numeros e vai
# coloca-los dentro da lista e a segunda vai mostrar a soma entre todos os valo
# res PARES sorteados pela função anterior.

# Importa as bibliotecas necessárias
from random import randint  # Para gerar números aleatórios
from time import sleep  # Para criar pausas/delay


# Função que sorteia 5 números aleatórios e adiciona à lista
def sorteia(lista):
    print(
        " Sorteando 5 valores da lista: ", end=""
    )  # Mensagem inicial sem quebra de linha
    for cont in range(0, 5):  # Loop para sortear 5 números
        n = randint(1, 10)  # Gera número aleatório entre 1 e 10
        lista.append(n)  # Adiciona o número à lista
        print(f"{n} ", end="", flush=True)  # Mostra o número sorteado
        sleep(0.5)  # Pausa de 0.5 segundos
    print("PRONTO!")  # Mensagem final


# Função que soma os valores pares de uma lista
def somaPar(lista):
    soma = 0  # Inicializa a soma
    for valor in lista:  # Percorre cada valor da lista
        if valor % 2 == 0:  # Verifica se o valor é par
            soma += valor  # Adiciona o valor par à soma
    print(f"Somando os valores pares de {lista}, temos {soma}")  # Resultado


# Programa principal
numeros = list()  # Cria lista vazia
sorteia(numeros)  # Chama função para sortear números
somaPar(numeros)  # Chama função para somar pares
