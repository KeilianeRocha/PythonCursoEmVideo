# TODO: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possivies sobre ele.

txt = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(txt))
print('So tem espaços?', txt.isspace())
print('É um número?', txt.isnumeric())
print('É alfabéico?', txt.isalpha())
print('É alfanumérico?', txt.isalnum())
print('Está em minúscula?', txt.islower())
print('Está em maiúscula?', txt.isupper())
print('Está capitalizado?', txt.istitle())










