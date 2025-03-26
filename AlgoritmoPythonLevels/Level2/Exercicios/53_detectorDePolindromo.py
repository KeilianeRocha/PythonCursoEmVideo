# TODO: Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
# desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper() # frase digitada, desconsidere os espaços antes e depois e coloca tudo em maiúscula
palavras = frase.split() # coloca a frase em uma lista(vetor)
junto = "-".join(palavras) # união da frase em uma única string
inverso = ""
print(f"O inverso de {junto} é {inverso}")
for letra in range(len(junto) - 1, -1, -1): # conta as letras começando da ultima -1 ate a primeira voltando -1 letra
    inverso += junto[letra]
if inverso == junto:
    print(f"A frase digitada é PALÍNDROMO")
else:
    print(f"A frase digitada não é PALÍNDROMO")

print(f"{' Fim do Programa ':=^30}")


# SEM USAR O FOR = USANDO FATIAMENTO DE STRING

"""
frase = (str(input("Digite uma frase: ")).strip().upper())
palavras = frase.split() 
junto = "-".join(palavras)
inverso = junto[::-1]
print(f"O inverso de {junto} é {inverso}")
# inverso = "" REMOVIDO
if inverso == junto:
    print(f"A frase digitada é PALÍNDROMO")
else:
    print(f"A frase digitada não é PALÍNDROMO")

print(f"{' Fim do Programa ':=^30}")
"""
