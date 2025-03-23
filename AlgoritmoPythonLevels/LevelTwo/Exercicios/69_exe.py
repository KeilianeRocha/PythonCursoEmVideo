# TODO:Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# quabtas mulheres tem menos de 20 anos.

from time import sleep


sexo = ''
menorIdade  = 0
maiorIdade = 0







print('-'*30)    
print("CADASTRE UMA PESSOA")
print("-" * 30)

idade = int(input("Idade: "))
sexo = str(input("Sexo: [M/F]")).strip().upper()
print("Cadastro realizado com sucesso!")

opcao = str(input("Quer continuar? [S/N]")).strip().upper()
print(" Analisando dados cadastrados...")
sleep(1)

print('-'*40)
print(f"Total de pessoas com mais de 18 anos: {menorIdade}")
print(f"Ao todo temos {sexo} homens cadastrados")
print(f"Há {maiorIdade} mulher com menos de 20 anos")

print(f"{'Fim do Programa ':=^30}")