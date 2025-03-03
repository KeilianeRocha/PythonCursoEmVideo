# TODO: Crie um programa que leia o nome de uma pessoa e diga se ele tem "Silva" no nome.

while True:
    name = str(input('Qual é o seu nome? ')).title().strip()
    if 'Silva' in name:
        print("Seu nome tem Silva? Sim!")
        break
    else:
        print('Seu nome não tem Silva. Tente novamente.')


