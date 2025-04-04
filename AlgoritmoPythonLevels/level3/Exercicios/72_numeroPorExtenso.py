# TODO: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero ate vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Importa a biblioteca num2words para converter números em palavras
from num2words import num2words

# O uso desse módulo evita a necessidade de criar manualmente uma tupla/dicionário com números por extenso

# Cria uma tupla com números de 0 a 20 (range(0, 21) gera 0,1,2...20)
contagem = tuple(range(0, 21))

# Loop infinito para garantir que o usuário digite um número válido
while True:
    # Solicita e converte a entrada para inteiro
    numero = int(input("Digite um número entre 0 e 20: "))

    # Verifica se o número está dentro do intervalo permitido
    if 0 <= numero <= 20:
        # Se válido, converte o número para extenso em português e exibe
        print("Você digitou o número ", num2words(numero, lang="pt_BR"))
        break  # Encerra o loop após sucesso
    else:
        # Mensagem de erro para números fora do intervalo
        print("Tente novamente. Digite um número entre 0 e 20: ")
