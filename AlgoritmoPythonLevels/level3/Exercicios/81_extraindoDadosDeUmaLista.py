# TODO: Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso, mostre:
# Quantos números foram digitados.
# Alista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e se está ou não na lista.
"""
 
 
 Você digitou 5 elementos.
 Os valores em ordem decescente são [x,x,x,x,x]
 O valor {x} fa parte da lista!
 
"""

"""
lista = []
opcao = ''


while True:
    numeros = int(input("Digite um valor: "))
    if numeros not in lista:
        lista.append(numeros)
        opcao = str(input("Quer continuar? [S/N] ")).split().upper()[0]
    if opcao in ['S', 'N']:
        break
print("Opção inválida! Digite S ou N.")  

print(lista)
numeros.sort[reverse=True]
"""

# MELHORIA DE CÓDIGO → AINDA NÃO ESTOU ENTENDENDO BEM ...

# Inicializa uma lista vazia para armazenar os valores digitados
lista = []

# Variável para controlar a opção de continuar/parar
opcao = ""

# Loop infinito (só para quando o usuário digitar 'N')
while True:
    # Adiciona o valor digitado (convertido para int) diretamente na lista
    lista.append(int(input("Digite um valor: ")))

    # Pega a opção do usuário, remove espaços, converte para maiúscula e pega a 1ª letra
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    # Se a opção for 'N', encerra o loop
    if opcao == "N":
        break
    # Se a opção NÃO for 'S', mostra mensagem de erro (mas continua o loop)
    elif opcao != "S":
        print("Opção inválida! Digite S ou N.")

# Mostra quantos elementos foram digitados
print(f" Você digitou {len(lista)} elementos.")

# Ordena a lista em ordem DECRESCENTE (reverse=True)
lista.sort(reverse=True)

# Mostra a lista ordenada
print(f"Os valores em ordem decrescente são {lista}")

# Verifica se o número 5 está na lista
if 5 in lista:
    print(f"O valor {5} faz parte da lista!")
else:
    print(f"O valor {5} não faz parte da lista!")
