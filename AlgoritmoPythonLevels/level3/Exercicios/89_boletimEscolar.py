# TODO: Faça um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.


# Cria uma lista vazia para armazenar os dados dos alunos
ficha = list()

# Loop infinito para cadastro de alunos
while True:
    # Solicita os dados do aluno
    nome = str(input("Nome:"))
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    nota3 = float(input("Nota 3:"))
    nota4 = float(input("Nota 4:"))

    # Calcula a média das notas
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # Adiciona os dados do aluno à ficha como uma lista [nome, [notas], média]
    ficha.append([nome, [nota1, nota2, nota3, nota4], media])

    # Pergunta se deseja continuar cadastrando
    opcao = (
        str(input("Dados cadastrados com sucesso! \nQuer continuar? [S/N]"))
        .strip()
        .upper()[0]
    )

    # Verifica a opção do usuário
    if opcao == "N":
        break  # Sai do loop de cadastro
    elif opcao != "S":
        print("Opção inválida! Digite S ou N.")

# Exibe o cabeçalho da tabela de alunos
print("-=" * 20)
print(f"{'N°':<4}{'NOME':<10}{'MEDIA':>8}")  # Formatação com alinhamento
print("-" * 25)

# Loop para exibir todos os alunos cadastrados
for indice, aluno in enumerate(ficha):
    # Mostra número, nome e média de cada aluno (formatado)
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:<8.1f}")

# Loop para consultar notas individuais
while True:
    print("-" * 25)
    # Solicita qual aluno ver as notas (999 para sair)
    opcao2 = int(input("Mostrar notas de qual aluno? (999 interrompe) "))

    if opcao2 == 999:
        print("FINALIZANDO...")
        break  # Encerra o programa

    # Verifica se o índice existe na lista
    if opcao2 <= len(ficha) - 1:
        # Exibe as notas do aluno selecionado
        print(f"Notas de {ficha[opcao2][0]} são {ficha[opcao2][1]}")
