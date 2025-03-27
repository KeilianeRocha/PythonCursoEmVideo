# TODO: Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import sample

aleatorio = tuple(sorted(sample(range(1, 100), 5)))
# 'sample' → Seleciona 5 elementos únicos
# 'sorted' → Ordena os números em ordem crescente.
print(f"Os valores sorteados foram: {aleatorio}")
print("O maior valor sorteado foi",min(aleatorio))
print("O menor valor sorteado foi",max(aleatorio))


# FIXME: Corrigir cod.
