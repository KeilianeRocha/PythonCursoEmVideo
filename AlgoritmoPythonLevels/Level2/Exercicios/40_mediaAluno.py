# TODO: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
    # - Média abaixo de 5.0 ==> REPROVADO!
    # - Média entre 5.0 e 6.9 ==> RECUPERAÇÃO
    # - Média 7.0 ou superior ==> APROVADO

notaOne = float(input("Digite a 1° nota:"))
notaTwo = float(input("Digite a 2° nota: "))
media = (notaOne + notaTwo) / 2
print(f"Tirando {notaOne} e {notaTwo}, a média do aluno é {media}")

if 7 > media >= 5:
    print("O aluno está RECUPERAÇÃO!")
elif media < 5.0:
    print("O aluno está de REPROVADO!")
elif media >= 7.0:
    print("O aluno está de APROVADO!")
print(f"{'Fim do Programa ':=^30}")
