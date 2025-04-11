# TODO: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# Matriz 3x3 (3 linhas, 3 colunas)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # evito que use o .append

# esse 1° 'for' é de alimentação
for l in range(0, 3): # laço de linhas
    for c in range(0, 3): # laço de colunas
        matriz[l][c] = int(input(f"Digite um valor [{l}, {c}]: "))
# esse 2° 'for' é para mostrar a estrutura        
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='') # uso de formatação centralizada ':^5'
    print() # quebra a linha
        