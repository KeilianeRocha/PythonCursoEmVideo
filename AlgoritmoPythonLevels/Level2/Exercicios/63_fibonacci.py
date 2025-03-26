# TODO: Escreva um programa que leia um numero n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma Seguência de Fibonacci.
"""exemplo_
0 =>1=>1=>2=>3=>5=>8
    """

print("-" *30)
print("Segiência de Fibonacci")
print("-" * 30)
n = int(input("Quantos termos você quer mostrar? "))  # Solicita ao usuário quantos termos da sequência de Fibonacci ele deseja ver. O valor é armazenado em 'N'
t1 = 0 
t2 = 1 
print("~"*30)
print(f"{t1} → {t2}", end="")  # Exibe os dois primeiros termos
cont = 3 # contador começa em 3, pois ja tenho os dois primeiros termos
while cont <= n:  # O loop continua enquanto 'cont' for menor ou igual a 'n'
    t3 = t1 + t2  # Calcula o próximo termo da sequência.
    print(f" → {t3} ", end="")
    t1 = t2  # Atualiza os valores de 't1' e 't2' para os próximos cálculos.
    t2 = t3 # ///
    cont += 1  # Incrementa o contador
print("Fim")
