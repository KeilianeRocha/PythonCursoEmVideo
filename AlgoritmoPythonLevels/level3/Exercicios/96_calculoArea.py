# TODO: Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangualar(largura e comprimento) e mostre as área
# do terreno.


# Define a função 'area' que calcula e exibe a área de um terreno
def area(larg, comp):
    a = larg * comp  # Calcula a área multiplicando largura pelo comprimento
    print(
        f"A área de um terreno {larg} x {comp} é de {a}m²."
    )  # Exibe o resultado formatado


# Programa principal
print("Controle de Terrenos.")  # Título do programa
print("-" * 20)  # Linha de separação para organização visual

# Recebe a largura do terreno como número decimal (float)
l = float(input("Largura (m): "))

# Recebe o comprimento do terreno como número decimal (float)
c = float(input("Comprimento (m): "))

# Chama a função 'area', passando a largura e o comprimento fornecidos
area(l, c)
