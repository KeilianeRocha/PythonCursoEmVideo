# TODO: Elabore um programa que calcule o valor a ser pago por um produto, considerando o
# seu preço normal e condição de pagamento:
# - À vista dinheiro/ pix/ cheque ==> 10% de desconto
# - À vista no cartão ==> 5% de desconto
# - Em até 2x no cartão ==> preço normal
# - 3x ou mais no cartão ==> 20% de juros

from time import sleep
TEMPO_ESPERA = 1

valor = float(input("Valor do produto R$"))
print("""Escolha a base de conversão:
    [1] - À VISTA DINHEIRO / PIX 
    [2] - À VISTA CARTÃO DE CRÉDITO
    [3] - EM ATÉ 2X NO CARTÃO
    [4] - 3X OU MAIS NO CARTÃO"""
    )
opcao = int(input("Seleciona a forma de pagamento): "))

print("PROCESSANDO...")
sleep(TEMPO_ESPERA)

if opcao == 1: 
    # print(f"Pagando à Vista Dineiro ou Pix o valor de R${produto:.2f} você recebe 10% de desconto e o valor do saldo fica R$", end='')
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)

elif opcao == 3: 
    total = valor
    parcela = valor / 2
    print(f"O valor {valor:.2f} parcelado em 2x é R${parcela:.2f}")
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totPacela  = int(input("Quantas parcelas? "))
    parcela = valor / totPacela
    print(f"O valor R${valor:.2f} parcelado em {totPacela}x é R${parcela:.2f} "
        f" - valor total a pagar R${total:.2f} *com juros")

else:
    total = valor
    print("Valor digitao inválido! Tente novamente...")

print(f"Sua compra vai custar R${total:.2f}")# esse print fora do laço vai acontecer sempre

print(f"{'OBRIGA E VOLTE SEMPRE! ':=^30}")
