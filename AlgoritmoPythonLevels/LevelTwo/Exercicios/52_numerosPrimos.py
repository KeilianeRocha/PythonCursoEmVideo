# TODO: Faça um programa que leia um número inteiro e diga se ele é ou não número primo.
"""_Explicação_
    São números naturais maiores que 1 que possuem exatamente 
    dois divisores distintos: o número 1 e ele mesmo. 
"""

num = int(input("Digite um número:"))
tot = 0
for c in range(1, num + 1): # range de 1 a numero + 1 prq o py descarta o último
    if num % c == 0:  # se num for divisível por c
        print("\033[33m", end='-')
        tot += 1 # incrementa o contador
    else:
        print("\033[31m", end="-")
    print(f"{c}",end='-')
print(f"\n\033[mO numero {num} foi divisível {tot} vezes")
if tot == 2: # Condição em que é True
    print("É por isso é PRIMO! ")
else:  # Condição em que é False
    print("Por isso NÃO é PRIMO")
