import math

# TODO: Crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada.

"""n = int(input('Digite um número: '))
print('O Dobro de {} é {}'.format(n, (n*2)))
print('O Triplo de {} é {}'.format(n, (n*3)))
print('a Raíz Quadrada de {} é {}'.format(n, (n**(1/2))))"""

# Ou colocando as váriaveis separadamente e usando a importação de módulo

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = math.sqrt(n)
print('O Dobro de {} é {}'.format(n, d))
print('O Triplo de {} é {}'.format(n, t))
print('a Raíz Quadrada de {} é {}'.format(n, math.ceil(r))) # arredondei pra cima
