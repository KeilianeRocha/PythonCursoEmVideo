# TODO: Faça um programa que leia uma frase pelo teclado e mostre:
# a) Quantas vezes aparece a letra "A"
# b) Em que posição ela aparece a primeira vez.
# c) Em que posição ela aparece a última vez.

phase = str(input('Digite uma frase: ')).upper().strip()
# 'UPPER' COLOCA A FRASE EM MAIÚSCULA
# 'STRIP' ELIMINA OS ESPAÇOS
print('A letra A aparece {} vezes na frase.'.format(phase.count('A')))
# 'COUNT' CONTA QUANTAS VEZES O 'A' APARECE
print('A primeira letra A apareceu na posição {}'.format(phase.find('A')+1))
# 'FIND' BUSCA O 'A' + 1
print('A última letra A apareceu na posição {}'.format(phase.rfind('A')+1))
# 'DFIND' BUSCA O 'A' DO LADO DIREITO
