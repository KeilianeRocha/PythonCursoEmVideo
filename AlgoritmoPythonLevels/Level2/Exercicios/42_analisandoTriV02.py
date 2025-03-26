# TODO:  Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que
# tipo de triângulo será formado:
    # - Equilátero ==> Todos os lados são iguais
    # - Isósceles ==> Dois lados iguais
    # - Escaleno ==> Todos os lados diferentes


""" _EXPLICAÇÃO_:
'if tri1 < tri2 + tri3 and tri2 < tri1 + tri3 and tri3 < tri1 + tri2: e o if e os elif '
subsequentes estão dentro do bloco do primeiro 'if (if tri1 < tri2 + tri3 and tri2 < tri1 + tri3 and tri3 < tri1 + tri2:)'.
Isso significa que esses blocos só serão avaliados se a condição '(if tri1 < tri2 + tri3 and tri2 < tri1 + tri3 and tri3 < tri1 + tri2:)'
for verdadeira.
"""

while True:
    tri1 = int(input("Primeiro Segumento: "))
    tri2 = int(input("Segundo Segumento: "))
    tri3 = int(input("Terceiro Segumento: "))

    if tri1 < tri2 + tri3 and tri2 < tri1 + tri3 and tri3 < tri1 + tri2:
        print(f"Os seguimentos acima PODEM FORMAR um triângulo ", end='') # Para o print abaixo ficar do lado do primeiro
        if tri1 == tri2 and tri2 == tri3: # ou tri1 == tri2 == tri3:
            print("EQUILÁTERO!")
        elif tri1 != tri2 and tri2 != tri3 != tri1: # ou tri1 != tri2 != tri3:
            print("ESCALENO!")
        else:
            print("ISÓSCELES!")
        break
    else:
        print("Os seguimentos não podem formar um TRIÂNGULO! Tente novamente...")
print(f"{'Fim do Programa ':=^30}")
