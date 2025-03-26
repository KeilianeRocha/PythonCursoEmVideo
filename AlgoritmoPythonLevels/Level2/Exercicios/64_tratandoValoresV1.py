# TODO: Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa so vai para quando o usuario digitar o valor 999, que é a condição
# de parada. No final, mostre quantos numeros foram digitados e qual foi a soma
# entre eles (desconsiderando o flag).


contador = 0  # Inicializa a soma total
total = 0  # Contador de números digitados

while True:
    num = int(input("Digite um número [999 para PARAR] "))
    if num == 999:  # Verifica se o usuário quer parar
        break
    total += num  # Adiciona o número à soma total
    contador += 1  # Incrementa o contador de números digitados

print(f"Você digitou {contador} números.")
print(f"A soma dos números digitados é {total}.")
print(f"{' Fim do Programa ':=^30}")

# '999' é uma condição de parada, quando executada o loop é encerado e as linhas 14 e 15 não são executadas
# portanto ele é eliminado da soma
# A linha 'total += num' só é executada se o número digitado não for '999'. Ele não é adicionado a variavel 'num'
