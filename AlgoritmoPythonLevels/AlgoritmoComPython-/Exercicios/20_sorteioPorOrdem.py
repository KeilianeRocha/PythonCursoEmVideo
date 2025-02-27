# TODO: O mesmo professor do desafio de n°(20) que sortear a  ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle

aluno1 = str(input('1° aluno: '))
aluno2 = str(input('2° aluno: '))
aluno3 = str(input('3° aluno: '))
aluno4 = str(input('4° aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f"A ordem de apresentação será:\n{lista}")

# print('A ordem de apresentação será')
# print(lista)
