# TODO: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex.
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
import math

numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
