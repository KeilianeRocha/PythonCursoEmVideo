# TODO: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# Quantas vezesapareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.



# Recebe 4 números de uma vez e já converte para inteiros, armazenando em uma tupla
num = (
    int(input("Digite um número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número:")),
    int(input("Digite o último número: ")),
)

# Variável tuple_conjunto comentada (não está sendo usada)
# tuple_conjunto = (num)

# Exibe todos os valores digitados
print(f"Você digitou os valores{num}")

# Conta quantas vezes o número 9 aparece na tupla
print(f"O valor 9 apareceu {num.count(9)} vezes")

# Verifica se o número 3 está presente na tupla
if 3 in num:
    # Se encontrado, mostra a posição (ajustando índice para começar em 1)
    print(f"O valor 3 apareceu {num.index(3)+1}° posição")
else:
    print(f"O valor 3 não foi digitado em nenhuma posição")

# Identifica e exibe números pares
print(f"Os valores pares digitados foram ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=",")  # Imprime os pares na mesma linha, separados por vírgula
