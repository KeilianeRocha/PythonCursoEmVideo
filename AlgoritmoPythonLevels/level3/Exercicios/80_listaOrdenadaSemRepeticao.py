# TODO:Crie um programa onde os usuario possa digitar cinco valores númericos e cadastre - os
# em uma lista, ja na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.


"""
lista = []

for c in range(1, 6):
    valor = int(input(f"Digite um valor: : "))
    print("Adicionado ao final da lista...")

    if valor >= 0:
        lista.append(valor)
        print(f"Adicionado na posição {c} da lista")

lista.sort()   
print(f"Os valores digitados em ordem foram {lista}")
"""

# MELHORIA NO CÓDIGO:

# Inicializa uma lista vazia para armazenar os valores
lista = []

# Loop para pedir 6 valores (de 0 a 5)
for c in range(0, 6):
    # Pede um valor inteiro ao usuário (repete 6 vezes)
    valor = int(input(f"Digite um valor: : "))

    # Verifica se é o PRIMEIRO valor digitado (c == 0) OU se é MAIOR que o último da lista
    if c == 0 or valor > lista[-1]:
        lista.append(valor)  # Adiciona ao FINAL da lista
        print("Adicionado ao final da lista...")

    # Se NÃO for o primeiro E NÃO for maior que o último:
    else:
        pos = 0  # Inicializa a posição como 0

        # Percorre a lista para encontrar onde inserir o valor
        while pos < len(lista):
            # Se o valor for MENOR/IGUAL ao valor atual da lista...
            if valor <= lista[pos]:
                lista.insert(pos, valor)  # Insere NA POSIÇÃO ATUAL
                print(f"Adicionado na posição {pos} da lista")
                break  # Sai do loop após inserir
            pos += 1  # Incrementa a posição se não encontrou ainda

# Exibe a lista final ordenada
print(f"Os valores digitados em ordem foram {lista}")
