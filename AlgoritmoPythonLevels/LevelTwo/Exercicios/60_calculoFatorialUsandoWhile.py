# TODO: Faça um programa que leia um número qualquer e mostre o seu fatorial
"""exemplo_
5! = 5x4x3x2x1 = 120
    """


 

num = int(input("Digite um número para calcular o fatorial: "))
contador = num
fatorial = 1

print(f"Calculando o fatorial de {num}! = ", end="")
while contador > 0:
    print(f"{contador}", end='')
    print(" x " if contador > 1 else " = ", end='')
    fatorial *= contador
    contador -= 1
print(fatorial)

print(f"{' Fim do Programa ':=^30}")
