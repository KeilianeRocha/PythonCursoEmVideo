# TODO: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero ate vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

from num2words import num2words


contagem = tuple(range(0, 21))  # Cria uma tupla com números de 0 a 20
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:  # Verifica se o número está na tupla
        print("Você digitou o número ",num2words(numero, lang="pt_BR"))
        break
    else:
        print("Tente novamente. Digite um número entre 0 e 20: ")

# FIXME: Corrigir cod.
