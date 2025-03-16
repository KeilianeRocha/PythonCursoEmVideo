# TODO: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.
mediaIdade = 0
somaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ""
totMulher20 = 0


for pessoa in range(1, 5):  
    print(f"----- {pessoa}° Pessoa  -----")
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("idade: "))
    sexo = str(input("Sexo [M/F] ")).strip()
    somaIdade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1


mediaIdade = somaIdade / pessoa
print(f"A média de idade do grupo é de {mediaIdade} anos")
print(f"O homem mais velhor tem {maiorIdadeHomem} anos e se chama {nomeMaisVelho}")
print(f"A quantidade de mulheres MENOS de 20 anos é {totMulher20}")
