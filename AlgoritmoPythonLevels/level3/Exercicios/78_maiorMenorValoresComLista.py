# TODO: Faça um programa que leia 5 valores numéricos e guarde- os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
# posições na lista.


# Codigo comentado

# Lista vazia para armazenar os valores digitados pelo usuário
lista = []

# Inicialização de 'maior' e 'menor' com 0 pode dar problema se todos os valores forem negativos
# (mas funciona no seu caso, pois você sobrescreve esses valores no primeiro input)
maior = 0
menor = 0

# Loop para pedir 5 valores (de 1 a 5) - range(1, 6) gera cont = 1, 2, 3, 4, 5
for cont in range(1, 6):
    # Input formatado para pedir valores em posições de 1 a 5
    valor = int(input(f"Digite um valor para a posição {cont}° : "))
    lista.append(valor)  # Adiciona o valor à lista

    # Define 'maior' e 'menor' no primeiro valor digitado (cont == 1)
    if cont == 1:
        maior = menor = valor
    else:
        # Atualiza 'maior' se o novo valor for maior que o atual
        if valor > maior:
            maior = valor
        # Atualiza 'menor' se o novo valor for menor que o atual
        if valor < menor:
            menor = valor

# Mostra a lista completa digitada pelo usuário
print(f"Você digitou os valores{lista}")

# Procura as POSIÇÕES do maior valor na lista
print(f"O maior valor digitado foi {maior} na posição ", end="")
for i, v in enumerate(lista):  # 'i' = índice (0,1,2...), 'v' = valor
    if v == maior:
        print(f"{i+1}...", end="")  # i+1 ajusta para contagem humana (1 a 5)
print()  # Pula linha após mostrar todas as posições do maior

# Mesma lógica para o menor valor
print(f"O menor valor digitado foi {menor} na posição ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i+1}...", end="")
print()  # Pula linha final
