# TODO: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo;
# - Abaixo de 18.5 ==> Abaixo do peso
# - entre 18.9 e 24.9 ==> Peso ideal
# - entre 25.9 e 29.9 ==> Sobrepeso
# - entre 30. e 34.9 ==> Obesidade classe I
# - entre 35.0 e 39.9 ==> Obesidade classe II
# - Acima de 40 ==> Obesidade classe III

while True:
    peso = float(input("Digite seu peso (Kg) "))
    altura = float(input("Digite sua altura (M) "))
    imc = peso / (altura ** 2)

    if imc < 18.5:  # < == MENOR
        print(f"Seu IMC é de {imc:.1f}: " ,end='')
        print("ABAIXO do PESO")
    elif 18.5 <= imc <= 24.9:
        print(f"Seu IMC é de {imc:.1f}: " ,end='')
        print("PESO ADEQUADO")
    elif 25 <= imc <= 29.9:
        print(f"Seu IMC é de {imc:.1f}: " ,end='')
        print("SOBREPESO PESO!")
    elif 30 <= imc <= 34.9:
        print(f"Seu IMC é de {imc:.1f}: " ,end='')
        print("OBESIDADE CLASSE I!")
    elif 35 <= imc <= 39.9:
        print(f"Seu IMC é de {imc:.1f}: " ,end='')
        print("OBESIDADE CLASSE II!")
    else:
        print(f"Seu IMC é de {imc:.1f}: " ,end='')
        print("OBESIDADE CLASSE III!")
    break

print("Classificação segundo a OMS a partir do IMC.")
print(f"{'Fim do Programa ':=^30}")


"""
    > == MAIOR
    < == MENOR
    """
novoSalario = salario + (salario * 15 / 100)