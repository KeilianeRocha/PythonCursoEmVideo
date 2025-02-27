#TODO: Crie um programa que leia um número Real qualquer pelo computador e mostre na tela a sua porção inteira."""

# Importando a biblioteca completa
import math 

n = float(input('Digite um valor: '))
print(f"O valor digitado foi {n} e sua porção inteira é {math.trunc(n)}")
#print('O valor digitado foi {} e sua porção inteira é {}'.format(n, math.trunc(n))) # 'TRUNC' CORTA A PARTE INTEIRA


""" Importando somente um módulo da biblioteca
from math import trunc

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, trunc(n)))
"""

""" Sem importação
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {:.0f}'.format(n, n))
"""

""" Usando uma função interna do Python
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, int(n)))
"""
