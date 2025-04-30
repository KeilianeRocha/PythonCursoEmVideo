# TODO: Faça um programa que tenha uma função chamada maior(), que receba vários
# parametros com valores inteiros.
# Seu programa tem que analizar todos os valores e dizer qual deles é o maior.


# Importa a função sleep do módulo time para criar pausas
from time import sleep


# Define a função maior que aceita quantidade variável de argumentos
def maior(*num):
    cont = maior = 0  # Inicializa contador e variável para armazenar o maior valor
    print("=" * 30)  # Imprime linha divisória
    print(f"Analisando os valores passados...")  # Mensagem de análise

    # Loop através de todos os valores passados
    for valor in num:
        print(f"{valor}", end=" ", flush=True)  # Imprime cada valor com espaço
        sleep(0.5)  # Pausa de 0.5 segundos entre cada valor

        # Verifica se é o primeiro valor (cont == 0)
        if cont == 0:
            maior = valor  # Define o primeiro valor como maior inicialmente
        else:
            if valor > maior:  # Compara com o maior atual
                maior = valor  # Atualiza o maior valor se necessário
        cont += 1  # Incrementa o contador de valores

    # Imprime os resultados finais
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")


# Chamadas de teste da função com diferentes conjuntos de valores
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()  # Chamada sem argumentos

# TODO:  TEM UM PEQUENO ERRO NA LINHA 22
