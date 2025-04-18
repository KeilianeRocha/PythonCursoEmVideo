# TODO: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os(com idade) em um dicionario se por acaso o CTPS for diferente de zero,
# o dicionario recebera também o ano de contração e o salario. calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date, datetime

# Idade mínima para aposentadoria no Brasil
mulherAposentadoria = 62
homemAposentadoria = 65

cadastro = dict()  # OK – Dicionário criado

cadastro["nome"]= str(input("Nome: ")).capitalize()
cadastro["sexo"]= str(input("[M/F]")).strip().upper()[0]
anoNascimento = int(input("Ano de Nascimento(AAAA): "))

anoAtual = datetime.now().year
cadastro["idade"] = anoAtual - anoNascimento

cadastro["ctps"] = int(input("Carteira de Trabalho (0 = NÃO TEM) "))
if cadastro["ctps"] != 0:
    cadastro["contratacao"] = int(input("Ano de contratação: "))
    cadastro["salario"] = float(input("Salário: R$ "))

    # Calculando a idade restante até a aposentadoria com base no sexo
    if cadastro["sexo"] == "F":
        idade_aposentadoria = mulherAposentadoria
    elif cadastro["sexo"] == "M":
        idade_aposentadoria = homemAposentadoria
    else:
        print("Sexo inválido.")
        idade_aposentadoria = None

    if idade_aposentadoria:
        if cadastro["idade"] >= idade_aposentadoria:
            cadastro["aposentadoria"] = "Já pode se aposentar!"
        else:
            cadastro["aposentadoria"] = anoAtual + (
                idade_aposentadoria - cadastro["idade"]
            )

print("\nDados do cadastro:")
for k, v in cadastro.items():
    print(f"{k.capitalize()}: {v}")
