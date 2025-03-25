# TODO:Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
    # Quantas pessoas tem mais de 18 anos.
    # Quantos homens foram cadastrados.
    # quantas mulheres tem menos de 20 anos.

from time import sleep

totIdade = totHomem = totMulher = 0


while True:  
    print('-'*30) 
    print("CADASTRE UMA PESSOA")
    print("-" * 30)
    idade = int(input("Idade: "))
    sexo = " "
    #
    while sexo not in 'FM':
         sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    if idade >= 18:
        totIdade += 1
    if sexo in 'M':
        totHomem += 1
    if sexo in 'F' and idade < 20:
        totmMlher += 1
      
    opcao = ' '  # Padrão claro para validação:
# Indica visualmente que a variável será sobrescrita
# Mostra que é um valor temporário/inicial ' '
    while  opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N]")).strip().upper()[0]
        if opcao == 'N':
            print(" Analisando dados cadastrados...")
            sleep(1)
            break
          
    print(f"Total de pessoas com mais de 18 anos: {totIdade}")
    print(f"Ao todo temos {totHomem} homens cadastrados")
    print(f"Há {totMulher} mulher com menos de 20 anos")
    print("Cadastro realizado com sucesso!")
    print(f"{'Fim do Programa ':=^30}")
