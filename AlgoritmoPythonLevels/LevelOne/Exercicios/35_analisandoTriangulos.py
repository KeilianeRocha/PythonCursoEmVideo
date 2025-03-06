# TODO: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""_Regra_
 Para se formar um triângulo, cada seguimento tem que ser menor do que a soma do cumprimentos dos outros dois.
 """

while True:
    r1 = float(input("Primeiro seguimento: "))
    r2 = float(input("Segundo seguimento: "))
    r3 = float(input("Terceiro seguimento: "))
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print("Os seguimentos acima PODEM formar TRIÂNGULO")
        break
    else:
        print("Os seguimentos acima NÃO podem formar um TRIÂNGULO! Tente novamente.")
print(f"{' Fim do Programa ':=^30}")
