# TODO: Cire um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionario e todos os dicionarios em uma lista. No final, mostre:
# Quantas pessoas foramcadastroadas
# A média de idade do grupo.
# Uma lista com todas as mulheres.
# Uma lista com todas as pessoas com idade acima da média.

cadastro = list()  # Lista que vai guardar todos os dicionários de pessoas
pessoa = dict()  # Dicionário temporário para armazenar dados de uma pessoa
soma = media = 0  # Variáveis auxiliares para cálculo da média de idade

while True:
    pessoa.clear()  # Limpa os dados anteriores do dicionário antes de adicionar novos
    pessoa["nome"] = str(input("Nome: "))  # Lê o nome da pessoa e armazena

    # Validação do sexo: repete até que seja digitado 'M' ou 'F'
    while True:
        pessoa["sexo"] = str(input("[M/F] ")).strip().upper()[0]
        if pessoa["sexo"] in ["M", "F"]:
            break
        print("Opção inválida! Digite M ou .F")

    pessoa["idade"] = int(input("Idade: "))  # Lê a idade
    soma += pessoa["idade"]  # Soma a idade para depois calcular a média
    cadastro.append(
        pessoa.copy()
    )  # Adiciona uma cópia do dicionário à lista de cadastro

    # Validação da opção de continuar: repete até que seja digitado 'S' ou 'N'
    while True:
        opcao_continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if opcao_continuar in ["S", "N"]:
            break
        print("Opção inválida! Digite S ou N.")

    if opcao_continuar == "N":
        break  # Encerra o loop principal se a resposta for 'N'

print("-=" * 30)
print(
    f"A) Ao todo temos {len(cadastro)} pessoas cadastradas."
)  # Mostra o total de pessoas

media = soma / len(cadastro)  # Calcula a média de idade
print(
    f"B) A média de idade é de {media:5.2f} anos."
)  # Mostra a média com 2 casas decimais

# Mostra os nomes das mulheres cadastradas
print(f"C) As mulheres cadastradas foram ", end="")
for p in cadastro:
    if p["sexo"] == "F":  # Se o sexo for feminino
        print(f"{p['nome']} ", end="")
print()

# Mostra pessoas com idade acima da média
print(f"D) Lista das pessoas que estão acima da média: ")
for p in cadastro:
    if p["idade"] >= media:
        print(f"  ", end="")
        for k, v in p.items():  # Mostra os dados de cada pessoa acima da média
            print(f"{k} = {v}; ", end="")
        print()

print("<< ENCERRADO >>")  # Finalização do programa
