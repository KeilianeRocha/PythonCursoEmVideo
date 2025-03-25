# TODO: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor seão entregues.
# obs: Cosidere que o caixa possui cédulas de R$ 50,00 - R$ 20,00 - R$ 10,00 e R$ 1,00


import random


valor_saque = int(input("Que valor você quer sacar? "))

for nota in [50, 20, 10, 1]:
    if valor_saque >= nota:
        qnt = valor_saque // nota
        valor_saque -= qnt * nota
        print(f"Total de {qnt} cédulas de R${nota}") 

print("Volte sempre ao BANCO CEV! Tenha um bom dia!")

