# TODO: Crie um programa onde o usuário possa digitar vários valores númericos e cadastre -os
# em uma lista. Caso o número ja exista lá denro, ele nãosera adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Melhorias: → Se o usuário digitar abc, o programa quebra.
# Solução futura: Use try/except para evitar erros:

# Lista vazia para armazenar os números digitados
numeros = list()
# Variável para controlar a continuação do loop
opcao = ''

# Loop infinito (só para quando o usuário digitar 'N')
while True:
    # Input para receber um número inteiro
    n = int(input("Digite um valor: "))
    # Verifica se o número JÁ EXISTE na lista (evita duplicatas)
    if n not in numeros:
        numeros.append(n)  # Adiciona à lista se for único
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
        # Pergunta se quer continuar (converte para maiúscula e pega a 1ª letra)
    opcao = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if opcao in ['S','N']: # correção da adicionando loop para evitar resposta que não fossem 'S/N'
        break
    print("Opção inválida! Digite S ou N.") # Não segue se a condição não for atendida
numeros.sort()
# Imprime a lista final ordenada
print(f"Você digitou os valores{numeros}")
