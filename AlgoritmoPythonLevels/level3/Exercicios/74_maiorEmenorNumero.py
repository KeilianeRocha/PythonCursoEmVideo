# TODO: Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


# Importa a função 'sample' do módulo random para sorteio sem repetição
from random import sample

# Gera uma tupla com 5 números únicos, ordenados:
# 1. 'range(1, 100)' → Cria um intervalo de 1 a 99
# 2. 'sample(..., 5)' → Seleciona 5 elementos únicos aleatoriamente
# 3. 'sorted()' → Ordena os números em ordem crescente
# 4. 'tuple()' → Converte o resultado em tupla (imutável)
aleatorio = tuple(sorted(sample(range(1, 100), 5)))

# Exibe os valores sorteados formatados
print(f"Os valores sorteados foram: {aleatorio}")

# Mostra o menor valor usando a função 'min()'
print("O menor valor sorteado foi", min(aleatorio))

# Mostra o maior valor usando a função 'max()'
print("O maior valor sorteado foi", max(aleatorio))
