# TODO: Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artificio, indo de 10 até 0, com uma pausade de 1 segundo entre eles.

from time import sleep

for cont in range(10, -1, -1):  # Sempre em um range o ultimo termo é ignorado, por isso a contagem não pode ser 10, 0, -1, ele vai retornar de 10 ate 1
    print(cont)
    sleep(0.75)
print("BUM! BUM! POOW!")


