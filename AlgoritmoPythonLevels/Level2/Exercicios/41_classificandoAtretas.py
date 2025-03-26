# TODO: A confederação de natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    # - Até 9 anos ==> MIRIM
    # - Até 14 anos == INFANTIL
    # - Até 19 anos ==> JUNIOR
    # - Até 20 anos ==> SENIOR
    # - Acima ==> MASTER

from datetime import date

anoNasc = int(input("Digite o ano de nascimento do aluno (AAAA) "))
idadeAtual = date.today().year
idade = idadeAtual - anoNasc
print(f" O atreta tem {idade} anos")

if idade <= 9: # MENOR OU IGUAL A 9
    print(f"Classificação: MIRIM")
elif idade <= 14:
    print(f"Classificação: INFANTIL")
elif idade <= 19:
    print(f"Classificação: JUNIOR")
elif idade <= 20:
    print(f"Classificação: SENIOR")
else:
    print(f"Classificação: MASTER")
print(f"{'Fim do Programa ':=^30}")
