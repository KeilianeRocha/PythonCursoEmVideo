# TODO: Escreva dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não exite valor maior, os dois são iguais


from time import sleep


while True:
    varOne = int(input("Digite o 1° valor : "))
    varTwo = int(input("Digite o 2° valor : "))
    TEMPO_ESPERA = 2
    print("PROCESSANDO...")
    sleep(TEMPO_ESPERA)
    if varOne > varTwo: 
        print(f"O 1° valor é MAIOR que o 2° valor")
    elif varTwo > varOne:
        print(f"O 2° valor é MAIOR que o 1° valor")
    elif varOne == varTwo or varTwo == varOne: 
        # Opcional, pois é possivel ir direto para o 'else' ou usar 'varOne == varTwo'
        print(f"Os dois valores são iguais")
        break
    else:
        print("Opção inválida!")
print(f"{' Fim do Programa ':=^30}")
