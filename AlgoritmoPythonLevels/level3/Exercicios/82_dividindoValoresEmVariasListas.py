# TODO: Crie um programa que vai ler vários numeros e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.


# Inicializa uma lista principal vazia
lista = []

# Variável para controle de continuidade
opcao = ""

# Listas separadas para números pares e ímpares
pares = list()
impares = list()

# Loop infinito para entrada de dados
while True:
    # Adiciona número digitado (convertido para int) à lista principal
    lista.append(int(input("Digite um número: ")))

    # Pega a opção do usuário, padronizando para maiúscula e pegando apenas 1º caractere
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    # Condição de saída do loop
    if opcao == "N":
        break
    # Mensagem para opção inválida (mas não impede a continuação)
    elif opcao != "S":
        print("Opção inválida! Digite S ou N.")

# Loop para separar pares e ímpares
for i, v in enumerate(lista):
    # Verifica se o número é par (resto da divisão por 2 == 0)
    if v % 2 == 0:
        pares.append(v)  # Adiciona à lista de pares
    else:
        impares.append(v)  # Adiciona à lista de ímpares

# Exibe os resultados
print(f"A lista completa é {lista}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")
