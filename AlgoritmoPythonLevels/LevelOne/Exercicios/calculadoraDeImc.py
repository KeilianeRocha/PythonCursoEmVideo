peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura**2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "ABAIXO do PESO"
elif 18.5 <= imc <= 24.9:
    classificacao = "PESO ADEQUADO"
elif 25 <= imc <= 29.9:
    classificacao = "EXCESSO de PESO"
elif 30 <= imc <= 34.9:
    classificacao = "OBESIDADE CLASSE I"
elif 35 <= imc <= 39.9:
    classificacao = "OBESIDADE CLASSE II"
else:
    classificacao = "OBESIDADE CLASSE III"

    # Exibição do resultado
print(f"Seu IMC: {imc:.1f} => {classificacao}")
print("Classificação segundo a OMS a partir do IMC.")


