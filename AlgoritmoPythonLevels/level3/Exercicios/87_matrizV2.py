# TODO: Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior dos valor da segunda linha.

# Matriz 3x3 (3 linhas, 3 colunas)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # evito que use o .append
# Sugestão: Poderia usar compreensão de lista: matriz = [[0]*3 for _ in range(3)]
soma_pares = maior = soma_colun = 0

# esse 1° 'for' é de alimentação
for l in range(0, 3):  # laço de linhas
    for c in range(0, 3):  # laço de colunas
        matriz[l][c] = int(input(f"Digite um valor [{l}, {c}]: "))
        # Sugestão: Adicionar tratamento de erro para valores não numéricos

# esse 2° 'for' é para mostrar a estrutura
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")  # uso de formatação centralizada ':^5'
        # Sugestão: Poderia usar constantes para o tamanho do alinhamento
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()  # quebra a linha

print(f"A soma dos valores PARES é {soma_pares}")

for l in range(0, 3):
    soma_colun += matriz[l][2]  # A coluna '2'
    # Sugestão: Tornar o índice da coluna configurável (variável)
print(f"A soma dos valores da 3° coluna é {soma_colun}")

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
    # Sugestão: Usar max() para encontrar o maior valor: maior = max(matriz[1])
print(f"O maior dos valor da segunda linha é {maior}")
