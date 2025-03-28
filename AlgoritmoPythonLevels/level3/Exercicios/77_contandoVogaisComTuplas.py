# TODO: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.



palavras = ('aprender', 'programar', 'python', 'linguagem', 'curso', 'gratis', 'estudar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f"\nNa palvras {p.upper()} temos → ", end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

