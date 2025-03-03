# TODO: Faça um programa que leia três números e mostre qual é o maior e qual é o menor

from time import sleep

while True:
    varOne = int(input("Digite o 1° valor : "))
    varTwo = int(input("Digite o 2° valor : "))
    varThree = int(input("Digite o 3° valor : "))
    TEMPO_ESPERA = 3
    menor = varOne
    print("PROCESSANDO...")
    sleep(TEMPO_ESPERA)
    if varTwo < varOne and varTwo < varThree:
        menor = varTwo
    if varThree < varOne and varThree < varTwo:
        menor = varThree
        break
    maior = varOne
    if varTwo > varOne and varTwo > varThree:
        maior = varTwo
    if varThree > varOne and varThree > varTwo:
        maior = varThree
    print(f"O MENOR valor digitado foi {menor}")
    print(f"O MAIOR valor digitado foi {maior}")
print(f"{' Fim do Programa ':=^30}")
