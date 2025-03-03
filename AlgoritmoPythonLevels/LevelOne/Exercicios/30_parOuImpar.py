# TODO: Crie um programa que leia um númeero inteiro e mostre na tela se ele pe PAR ou ÍMPAR.

"""_Regra_:
Um número é par se for divisível por 2 (ou seja, o resto da divisão por 2 é 0).
Caso contrário, o número é ímpar."""


numero = int(input("Mediga um número qualquer: "))
if numero % 2 == 0:
    print(f"O número {numero} é PAR")
else:
    print(f"O número {numero} é ÍMPAR.")
print(f"{' Fim do Programa ':=^30}")
