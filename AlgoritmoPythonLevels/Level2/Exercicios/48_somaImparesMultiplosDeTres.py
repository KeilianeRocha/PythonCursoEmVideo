# TODO: Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e
# que se encontram no intervalo de 1 até 500.

soma = 0 # conceito de acomulador
for numero in range (1, 501, 2): # com 2 ele vai pulando 2
    if numero % 3 == 0:
        soma = soma + numero # soma recebe ela e soma com o resultado de 'numeros'
print(soma) # Mostra a soma de todos os valores divisiveis por 3 no intervalo de 1 a 501
        #print(numero,end=' - ') // mostra todos os valores divisivéis por 3 no intervalo de 1 a 501
print(f"{' Fim do Programa ':=^30}")
