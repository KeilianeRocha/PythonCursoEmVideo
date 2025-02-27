# TODO: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o 
# primeiro nome e o último nome separadamente.
# ex.
# Ana Maria de Souza
# primeiro = Ana
# último = Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
# 'SPLIT' FATIA O NOME DENTRO DE UMA LISTA [0,1,2,...]
print('Seu primeiro nome é {}'.format(nome[0]).title())
# 'TITLE' DEIXA SOMENTE A 1° LETRA MAIÚSCULA
print('O seu último nome é {}'.format(nome[len(nome)-1]).title())
# 'LEN' MOSTRA A POSIÇÃO DENTR DA LISTA -1

