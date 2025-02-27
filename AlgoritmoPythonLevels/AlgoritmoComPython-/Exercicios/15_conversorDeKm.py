# TODO: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km  rodados? '))
aluguel = (d * 60) + (km * 0.15)
print(f"O carro foi alugado por {d} dias, e você percorreu {km}km,\nO total a ser é pago de R${aluguel:.2f}")

# print('O carro foi alugado por {} dias, e você percorreu {}km,\n'
#       'O total a ser é pago de R${:.2f}'.format(d, km, aluguel))
