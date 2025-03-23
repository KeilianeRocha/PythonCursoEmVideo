# TODO: Faça um programa que mostre a tabuada de vários numeros,
# um de cada vez, para cada valor digitado pelo usuário. O programa
# será interrompido quando o número solicitado for negativo.


print("-" * 35)

while True:
    num = int(input("Quer ver a tabuada de que número? "))
    print("-" * 35)
    
    if num < 0:
        print("PROGRAMA TABUADA ENCERRADO.")  
        break  
    
    for c in range(1, 11):
        tabuada = num * c
        print(f"{num} x {c} = {tabuada}")
print("-" * 35)



