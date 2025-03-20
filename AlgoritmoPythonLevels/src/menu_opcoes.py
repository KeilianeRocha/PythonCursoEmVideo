def somar(n1, n2):
    return n1 + n2


def multiplicar(n1, n2):
    return n1 * n2


def maior(n1, n2):
    return max(n1, n2)


def menu():
    print(
        """
        [ 1 ] - SOMAR
        [ 2 ] - MULTIPLICAR
        [ 3 ] - MAIOR
        [ 4 ] - NOVOS NÚMEROS
        [ 5 ] - SAIR DO PROGRAMA
        """
    )


def main():
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))

    opcao = 0  # Inicializa a variável opcao

    while opcao != 5:  # Continua o loop até o usuário escolher a opção 5 (SAIR)
        menu()
        opcao = int(input("Qual é a sua opção? "))
        if opcao == 1:
            resultado = somar(n1, n2)
            print(f" A soma entre {n1} e {n2} é {resultado}")
        elif opcao == 2:
            resultado = multiplicar(n1, n2)
            print(f" O produto entre {n1} e {n2} é {resultado}")
        elif opcao == 3:
            resultado = maior(n1, n2)
            print(f"Entre o valor {n1} e {n2} o maior valor é {resultado}")
        elif opcao == 4:
            print("Informe os números novamente: ")
            n1 = int(input("Primeiro valor: "))
            n2 = int(input("Segundo valor: "))
        elif opcao == 5:
            print("Finalizando...")
        else:
            print("Opção inválida! Digite um valor válido!")
        print("=-=" * 10)
    print(f"{' Fim do Programa ':=^30}")


if __name__ == "__main__":
    main()
