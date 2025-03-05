# TODO: Escreva um programa que leia um número qualquer inteiro e peça para o usuário escolher qual será a base de conversão:
# - 1 para binario;
# - 2 para octal
# - 3 para hexadecimal

while True:
    numero = int(input("Digite um número inteiro: "))

    # Solicita a opção de conversão
    print(
        '''Escolha a base de conversão:")
    [1] - Binário
    [2] - Octal
    [3] - Hexadecimal
    [4] - Sair'''
    )
    opcao = int(input("Digite a opção (1, 2 ou 3 4 para sair): "))
    print(f"Sua opção foi {opcao}")
    # Realiza a conversão de acordo com a opção escolhida
    if opcao == 1:
        resultado = bin(numero)  # Converte para binário
        print(f"O número {numero} em binário é: {resultado[2:]}") # Usando o fatiamento de 'strig' do indice [2:] ':' ate o final dela
        break
    elif opcao == 2:
        resultado = oct(numero)  # Converte para octal
        print(f"O número {numero} em octal é: {resultado[2:]}")
        break
    elif opcao == 3:
        resultado = hex(numero)  # Converte para hexadecimal
        print(f"O número {numero} em hexadecimal é: {resultado[2:]}")
        break
    elif opcao == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Escolha 1, 2 ou 3 ou 4 para sair.")
print(f"{' Fim do Programa ':=^30}")
