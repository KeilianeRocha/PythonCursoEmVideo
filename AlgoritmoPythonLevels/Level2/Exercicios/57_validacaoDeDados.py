# TODO: Faça um programa que leia o sexo de uma pessoa, mas sp aceite os valores 'M' e 'F'.
# caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''

while sexo != "M" and sexo != "F":  # Continua pedindo até o usuário digitar 'M' ou 'F'
    sexo = str(input("A pessoa é do sexo [F/M]? ")).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print(f"Erro! tente novamente...")
    else:
        if sexo == 'M':
            print(f"O individuo é do sexo MASCULINO")
        elif sexo == 'F':
            print("O individuo é do sexo FEMININO")
print(f"{'Fim do Programa ':=^30}")
