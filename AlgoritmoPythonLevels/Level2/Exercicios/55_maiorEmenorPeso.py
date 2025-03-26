# TODO: Faça um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lido.

totMaior = 0
totMenor = 0

for pessoa in range(1, 6):
    peso = float(input(f"Digite o peso kg da {pessoa}°: "))
    # Inicializa totMaior e totMenor com o primeiro peso
    if pessoa ==1:
        totMaior = peso
        totMenor = peso
    else:
        # Atualiza totMaior e totMenor
        if peso > totMaior:
            totMaior = peso
        if peso < totMenor:
            totMenor = peso
print(f"O MAIOR peso lido foi {totMaior}kg")
print(f"O MENOR peso lido foi {totMenor}kg")

print(f"{'Fim do Programa ':=^30}")
