# TODO: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tange = tan(radians(angulo))
print(
    f"O ângulo de {angulo} tem o SENO de {seno:.2f}\n"
    f"O ângulo de {angulo} tem o COSSENO de {coss:.2f}\n"
    f"O ângulo de {angulo} tem a TANGENTE de {tange:.2f}"
)

# print('O ângulo de {} tem o SENO de {:.2f}\n O ângulo de {} tem o COSSENO de {:.2f}\n'
#       'O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, seno, angulo, coss, angulo, tange))
