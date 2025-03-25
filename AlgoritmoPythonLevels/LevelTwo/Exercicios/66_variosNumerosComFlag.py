# TODO: Crie um programa que leia vários números inteiros pelo teclado.
# O programa so vai para qquando o unsuário digitar o valor [999], que
# é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag '999').

num = soma = cont = 0


while num != 999:
    num = int(input("Digite um valor [999 para PARAR]"))
    if num == 999: 
        break
    soma += num
    cont += 1 
print(f"Você digitou {cont} números.")
print(f" A soma dos {cont} valores foi {soma}")
print(f"{' Fim do Programa ':=^30}")
