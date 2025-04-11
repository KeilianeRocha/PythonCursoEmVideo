# TODO: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre
# os valores pares e ímpares em ordem crescente.

num = [[], []]  # num[0] para pares, num[1] para ímpares
valor = 0
# pares = impares = 0

for c in range(1,8):
    valor = int(input(f"Digite o {c}° valor: "))
    num.sort()
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
# Ordena cada sublista separadamente APÓS a coleta
num[0].sort()  # Ordena os pares
num[1].sort()  # Ordena os ímpares
print()
print(f"Os valores pares digitados foram {num[0]}")
print(f"Os valores ímpares digitados foram {num[1]}")
print(f"Todos os valores digitados: {num[0] + num[1]}")
