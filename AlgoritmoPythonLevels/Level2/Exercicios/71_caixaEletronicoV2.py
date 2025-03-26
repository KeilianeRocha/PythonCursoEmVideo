# TODO: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor seão entregues.
# obs: Cosidere que o caixa possui cédulas de R$ 50,00 - R$ 20,00 - R$ 10,00 e R$ 1,00


valor = int(input("Que valor você quer sacar? "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        totced += 1
        total -= ced
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")
