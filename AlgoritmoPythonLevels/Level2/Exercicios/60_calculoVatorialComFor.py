# TODO: Faça um programa que leia um número qualquer e mostre o seu fatorial
"""exemplo_
5! = 5x4x3x2x1 = 120
    """


from math import factorial  


num = int(input("Digite um número para calcular o fatorial: "))
fatorial = factorial(num)
print(f"Calculando o fatorial de {num}! = ", end="")
for c in range(num, 1, -1):
    print(c, end=' x ')
print("1 =", fatorial)

print(f"{' Fim do Programa ':=^30}")
