# TODO:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas
# b) O nome com todas as letras minúsculas
# c) Quantas letras ao todo (sem considerar espaços)
# d) Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

