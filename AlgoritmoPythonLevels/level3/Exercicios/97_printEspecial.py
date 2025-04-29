# TODO: Faça um programa que tenha uma função chamada escreva(), que receba um
# texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.
# p. exe.: escreva("Olá, mundo!")
# saida → Olá, mundo!


# Define a função 'escreva' que formata uma mensagem dentro de uma moldura
def escreva(msg):
    tam = (
        len(msg) + 4
    )  # Calcula o tamanho da moldura: comprimento da mensagem + 4 espaços extras
    print("~" * tam)  # Imprime a linha superior da moldura feita de tildes (~)
    print(f"  {msg}")  # Imprime a mensagem com dois espaços de margem à esquerda
    print("~" * tam)  # Imprime a linha inferior da moldura feita de tildes (~)


# Chama a função 'escreva' passando a mensagem "Olá, mundo!"
escreva("Olá, mundo!")
