# TODO: Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre
# a media entre todos os valores e qual foi o maior e o menor valor lido.
# O prgrama deve perguntar ao usuario se ele quer ou não continuar a digitar valores.


# Inicialização das Variáveis:
opcao = "S"
total = cont = media = maior = menor = 0

while opcao in 'Ss':
    num = int(input("Digite um número: "))
    total += num
    cont += 1
    if cont ==  1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input("Quer continuar? [S/N] ")).upper().strip()
media = total / cont # calculada aopos o loop

print(f"Você digitou {cont} números e a média foi {media:.1f}\n"
      f"O maior valor foi {maior} e o menor foi {menor}")
print(f"{' Fim do Programa ':=^30}")
