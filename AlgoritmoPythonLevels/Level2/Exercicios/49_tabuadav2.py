# TODO: Refaça o DESAFIO 09, mostando a tabuada de um número que o usuário escolher,
# so que agora utilizando o laço for.


print("{:=^30}".format("Calculadora"))  # '^' CENTRALIZA O TEXTO
n = int(input("Digite um número para ver sua tabuada: "))
for c in range(1, 11):
    print(f"{n} x {c} = {n*c}")
print("{:=^30}".format("Fim do Programa"))
