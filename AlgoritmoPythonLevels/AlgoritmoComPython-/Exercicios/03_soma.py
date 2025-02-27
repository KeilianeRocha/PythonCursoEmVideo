# TODO: Crie um script que leia dois numeros e tente mostrar a soma entre eles.

"""Código com erro

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma de ', n1, '+', n2, 'é igua a ', n1 + n2)
"""

"""
Não vai somar, vai unir
input() recebe uma entrada do usuário, como uma string
Para realizar a soma é necessário converter os valores para o tipo numérico
"""
# Código Corrigido

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
# print('A soma de', n1, '+', n2, 'é igua a ', soma)
# print('A soma de {} + {} é {}'.format(n1, n2, soma))
print('A soma de {0} + {1} é {2}'.format(n1, n2, soma)) # ordenando



