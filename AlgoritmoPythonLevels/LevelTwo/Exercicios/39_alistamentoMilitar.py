# TODO: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda va se alista ao serviço militar.
# - Se é a hora de se alistar.
# - Se ja passou do tempo do alistamento.
# TODO:Seu programa também deverá mostrar o tempo que falta ou que que passou do prazo.
# TODO: Adicione a opção de perguntar o sexo para saber se a pessoa pode ou não se alistar OBRIGATÓRIAMENTE (em caso de ser do sexo masculino)


from datetime import date

while True:
    # nome = str(input("Digite seu nome: "))
    nasAno = int(input("Digite o anos do seu nascimento (AAAA): "))
    atual = date.today().year
    idade = atual - nasAno

    if idade == 18:
        print(f"Você nasceu em {nasAno} e tem {idade}\nDeve se alistar IMEDIATAMENTE!")

    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print(
            f"Você nasceu em {nasAno} e tem {idade} anos de idade\n"
            f"Ainda faltam {saldo} anos para o seu alistamento que ocorrerá em {ano}.\n"
        )

    else:
        saldo = idade - 18
        ano = atual - saldo
        print(
            f"Você nasceu em {nasAno} e tem {idade} anos de idade\n"
            f"Você deveria ter se alistado há {saldo}\n"
            f"Seu alistamento foi em {ano}."
        )

        break
print(f"{'Fim do Programa ':=^30}")
