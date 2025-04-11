# TODO: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# Quantas pessoas foram cadastradas.
# Uma listagem com as pessoas mais pesadas.
# Uma listagem com as pessoas mais leves.


"""
// MEU CÓD COM ERROS  

pessoas =  list()
dados = list()
maior_peso = menor_peso = 0  # Inicializa sem valores # isso não serve pra listas.


while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
          totMaioPeso = totMenorPeso = dados[1]
     #else:
          if dados[1] > totMaioPeso:
               totMaioPeso = dados[1]
          if dados[1] < totMenorPeso:
               totMenorPeso = dados[1]
    pessoas.append([dados[:]])
    dados.clear()
    opcao = str(input("Cadastro realizado com sucesso!\n"
                      f"Quer continuar? [S/N]")).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao != "S":
        print("Opção inválida! Digite S ou N.")
     

print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {totMaioPeso} Kg. ")
print(f"O menor peso foi de {totMenorPeso} Kg. ")
"""

## CODIGO CORRIGIDO

pessoas = []  # Lista principal para armazenar todos os cadastros
maior_peso = menor_peso = None  # Inicializa sem valores

while True:
    # Coleta de dados
    nome = input("Nome: ")

    try:
        peso = float(input("Peso: "))
    except ValueError:
        print("Erro: Peso deve ser um número. Tente novamente.")
        continue

    # Adiciona à lista principal
    pessoas.append([nome, peso])

    # Atualiza maior e menor peso
    if maior_peso is None or peso > maior_peso:
        maior_peso = peso
    if menor_peso is None or peso < menor_peso:
        menor_peso = peso

    # Pergunta se deseja continuar
    resp = input("Quer continuar? [S/N] ").strip().upper()
    if resp == "N":
        break

# Exibe resultados
print("-" * 30)
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior_peso}kg. Peso de ", end="")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"[{p[0]}] ", end="")
print()  # Quebra de linha

print(f"O menor peso foi de {menor_peso}kg. Peso de ", end="")
for p in pessoas:
    if p[1] == menor_peso:
        print(f"[{p[0]}] ", end="")
print()  # Quebra de linha
