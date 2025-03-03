# TODO: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# 1. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# 2. R$0,45 para viagens mais longas.


distancia = float(input("Qual a ditância da viagem? "))
if distancia <= 200:
    preco = distancia * 0.50
    print(
        f"Você esta prestes a começar uma viagem de {distancia:.2f}Km pagando R${preco:.2f}"
    )
else:
    preco = distancia * 0.45
    print(
        f"Você esta prestes a começar uma viagem de {distancia:.2f}Km pagando R${preco:.2f}")
print(f"{' Fim do Programa ':=^30}")
