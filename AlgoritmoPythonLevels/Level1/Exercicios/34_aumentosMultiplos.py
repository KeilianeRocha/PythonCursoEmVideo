# TODO: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    # 1. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
    # 2. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input("Qual o salario do funcionário R$ "))
if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100)
    print(f"Quem ganhava R${salario:.2f} agora passa a ganhar R${novoSalario:.2f} agora.")
else:
    novoSalario = salario + (salario * 10 / 100)
    print(f"Quem ganhava R${salario:.2f} agora passa a ganhar R${novoSalario:.2f} agora.")
print(f"{' Fim do Programa ':=^30}")


novoSalario = salario + (salario * 15 / 100)