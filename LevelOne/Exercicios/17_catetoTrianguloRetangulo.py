#TADO: Faça um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o cumprimento da hipotenuza."""

from math import hypot

""" De forma manual
cOpost = float(input('Comprimento do cateto oposto: '))
cAdjac = float(input('Comprimento do cateto adjacente: '))
hi = (cOpost ** 2 + cAdjac ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
"""

cOpost = float(input('Comprimento do cateto oposto: '))
cAdjac = float(input('Comprimento do cateto adjacente: '))
hi = hypot(cOpost, cAdjac)
print(f"A hipotenusa vai medir {hi:.2f}")
#print('A hipotenusa vai medir {:.2f}'.format(hi))

