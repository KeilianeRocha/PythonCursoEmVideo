# TODO: Crie um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome "Santo".

# town = str(input('Em que cidade você nasceu? ')).upper().strip()
# print(town[:5] == 'SANTO')


while True: # ENUQNTO FOR VERDADEIRO FAÇA...
    town = str(input("Em que cidade você nasceu? ")).upper().strip()
    if town[:5] == "SANTO":  # Verifica se os primeiros 5 caracteres são "SANTO"
        print("Você nasceu em uma cidade que começa com 'Santo'!")
        break
    else:
        print("Você não nasceu em uma cidade que começa com 'Santo'. Tente novamente.")
