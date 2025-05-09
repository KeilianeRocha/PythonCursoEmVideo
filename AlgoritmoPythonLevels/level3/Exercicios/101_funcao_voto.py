# TODO: Crie um programa que tenha uma função chamada voto() que vai receber
# como parametro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto nas eleições.
# (a) NEGATO,
# (b) OPCIONAL
# (c) OBRIGATÓRIO


def voto (nasAno):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - nasAno
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA!"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL!"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO!"

# Programa principal
nasc = int(input("Em que ano você nasceu?(AAAA) "))
print(voto(nasc))