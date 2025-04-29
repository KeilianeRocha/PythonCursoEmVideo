# TODO: Faç um programa que tenha uma função chamada contador(), que receba três
# parâmetros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 e, 2
# C) Uma contagem personalizada.

from time import (
    sleep,
)  # Importa a função sleep, que faz o programa "dormir" (pausar) por um tempo


# Define a função 'contador' que faz uma contagem entre dois números com um passo definido
def contador(i, f, p):
    if p < 0:  # Se o passo for negativo, transforma em positivo
        p *= -1
    if p == 0:  # Se o passo for 0, muda para 1 (não pode ter passo 0)
        p = 1

    print(
        f"Contagem de {i} até {f} de {p} em {p}"
    )  # Mensagem mostrando o tipo de contagem

    # Se o início for menor que o fim, a contagem é crescente
    if i < f:
        cont = i  # Começa a contagem a partir de 'i'
        while cont <= f:
            print(
                f"{cont} ", end="", flush=True
            )  # Imprime o número na mesma linha, forçando a impressão imediata
            sleep(0.5)  # Pausa de 0.5 segundos para dar efeito de contagem
            cont += p  # Incrementa o contador
        print("FIM!")  # Mensagem de fim da contagem

    # Se o início for maior que o fim, a contagem é decrescente
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="", flush=True)  # Imprime o número
            sleep(0.5)  # Pausa para efeito
            cont -= p  # Decrementa o contador
        print("FIM!")  # Mensagem de fim da contagem


# Faz três contagens:
contador(1, 10, 1)  # Contagem automática de 1 até 10, de 1 em 1
contador(10, 1, 2)  # Contagem automática de 10 até 1, de 2 em 2

# Parte para contagem personalizada:
print("Personalize a contagem ")
ini = int(input("Início: "))  # Pede início ao usuário
fim = int(input("Fim:    "))  # Pede fim ao usuário
pas = int(input("Passo:  "))  # Pede passo ao usuário
contador(ini, fim, pas)  # Chama a função com os valores informados
