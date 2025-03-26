# TODO: Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do jogo
# Seu programa deverá realizar a operação solicitada em cada caso.


n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

opcao = 0  # Inicializa a variável opcao

while opcao != 5:  # Continua o loop até o usuário escolher a opção 5 (SAIR)

    print('''
        [ 1 ] - SOMAR
        [ 2 ] - MULTIPLICAR
        [ 3 ] - MAIOR
        [ 4 ] - NOVOS NÚMEROS
        [ 5 ] - SAIR DO PROGRAMA
        ''')
    opcao = int(input("Qual é a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print(f" A soma entre {n1} e {n2} é {soma}")
    elif opcao == 2:
        multiplica = n1 * n2
        print(f" O produto entre {n1} e {n2} é {multiplica}")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f"Entre o valor {n1} e {n2} o maior valor é {maior}")
    elif opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida! Digite um valor válido!")
    print('=-='*10)
print(f"{' Fim do Programa ':=^30}")
