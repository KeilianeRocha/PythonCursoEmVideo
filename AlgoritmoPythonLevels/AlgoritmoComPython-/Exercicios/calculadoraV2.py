# Tabuada
print('-' * 21 + '\n   Tabuada\n' + '-' * 21)
print("[1]=> ADIÇÃO\n[2]=> SUBTRAÇÃO\n[3]=> MULTIPLICAÇÃO\n[4]=> DIVISÃO")
escolha = int(input("Qual a tabuada que vc quer que eu resolva? "))
tabuada = int(input("Digite um número: "))
print("-" * 30)
if escolha == 1:
    n = 1
    while n < 11:
        soma = tabuada + n
        print("{} + {} = {}".format(tabuada, n,soma))
        n += 1
elif escolha == 2:
    n = 1
    while n < 11:
        subtracao = tabuada - n
        print("{} - {} = {}".format(tabuada, n, subtracao))
        n += 1
elif escolha == 3:
    n = 1
    while n < 11:
        multiplicacao = tabuada * n
        print("{} x {} = {}".format(tabuada, n, multiplicacao))
        n += 1
elif escolha == 4:
    n = 1
    while n < 11:
        divisao = tabuada / n
        print("{} / {} = {:.1f}".format(tabuada, n, divisao))
        n += 1
else:
    print("Opção INVÁLIDA, tente novamente.")
