# TODO: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


# Tupla contendo palavras para análise
palavras = (
    "aprender",
    "programar",
    "python",
    "linguagem",
    "curso",
    "gratis",
    "estudar",
    "trabalhar",
    "mercado",
    "programador",
    "futuro",
)

# Loop principal que percorre cada palavra na tupla
for p in palavras:
    # Typo em "palvras" (deveria ser "palavra")
    print(f"\nNa palvras {p.upper()} temos → ", end=" ")

    # Loop aninhado que verifica cada letra da palavra atual
    for letra in p:
        # Verifica se a letra é uma vogal (maiúscula ou minúscula)
        if letra.lower() in "aeiou":
            # Imprime a vogal encontrada (mantendo na mesma linha)
            print(letra, end=" ")
