# TODO: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""_Regra_
Regra para anos bissextos:
Um ano é bissexto se atender a uma das seguintes condições:

Divisível por 4, mas não divisível por 100.

Exemplo: 2004 é bissexto (divisível por 4 e não divisível por 100).

Divisível por 400.

Exemplo: 2000 é bissexto (divisível por 400).
"""
from datetime import date


ano = int(input("Que ano você gostaria de analisar? Digite 0 para inicializar o ano atual: "))
if ano == 0: # comando para inicailizar o ano atual
    ano = date.today().year #módulo de captura do ano atual
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0): # Formula de calculo apara ano bissexto
    print(f"o ano {ano} que você digitou é BISSEXTO") #condição True
else:
    print(f"o ano {ano} que você digitou  NÃO É BISSEXTO")  # condição False
print(f"{' Fim do Programa ':=^30}")
