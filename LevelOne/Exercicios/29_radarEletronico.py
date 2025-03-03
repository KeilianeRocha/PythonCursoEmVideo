# TODO: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que le foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = int(input("Qual a velocidade atual do carro? "))
if velocidade <= 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print(
        f"MULTADO! Você excedeu o limite permitido que é de 80Km/h\n"
        f"Você deve pagar uma multa de R$280.00!"
        )
print(f"{' Fim do Programa ':=^30}")
