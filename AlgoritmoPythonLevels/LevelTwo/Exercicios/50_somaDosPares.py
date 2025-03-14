# TODO: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        print(soma)
        soma += numero
        cont += + 1
print(f"Voce informou {cont} PARES e a soma foi {soma}")

print(f"{' Fim do Programa ':=^30}")
