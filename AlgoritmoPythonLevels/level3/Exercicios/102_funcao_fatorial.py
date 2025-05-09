# TODO: Crie um programa que tenha uma função fatorial() que receba dois
# parametros:
# o primeiro que indique o número a calcular
# O outro chamado shoow, que será um valor lógico (opcional) indicando se será
# mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
        -> Clacula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostra ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):  # -1 esta voltando casas decimais
        if show:
            print(c, end='')
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


# Programa principal

#print(fatorial(5, show=True))
help(fatorial)
