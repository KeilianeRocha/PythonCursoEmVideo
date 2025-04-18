# TODO: Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()  # Lista principal que vai armazenar os dados de todos os jogadores
jogador = dict()  # Dicionário para armazenar temporariamente os dados de um jogador
partidas = list()  # Lista que guarda a quantidade de gols de cada partida

while True:
    jogador.clear()  # Limpa os dados do dicionário antes de cada novo cadastro
    jogador["nome"] = str(
        input("Nome do jogador: ")
    ).capitalize()  # Solicita o nome e capitaliza a primeira letra
    tot = int(
        input(f"Quantas partidas {jogador['nome']} jogou? ")
    )  # Pergunta quantas partidas ele jogou
    partidas.clear()  # Limpa a lista de gols para novo jogador

    # Loop para registrar os gols em cada partida
    for c in range(0, tot):
        partidas.append(
            int(input(f"  Quantos gols na partida {c+1}? "))
        )  # Adiciona os gols da partida à lista

    jogador["gols"] = partidas[:]  # Copia a lista de gols para o dicionário do jogador
    jogador["total"] = sum(partidas)  # Calcula o total de gols e salva no dicionário

    time.append(
        jogador.copy()
    )  # Adiciona uma cópia do dicionário do jogador à lista principal `time`

    # Pergunta se o usuário quer continuar cadastrando
    while True:
        opcao_continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if opcao_continuar in ["S", "N"]:
            break
        print("Opção inválida! Digite S ou N.")

    if opcao_continuar == "N":
        break  # Encerra o cadastro se o usuário digitar N

# Exibe cabeçalho da tabela
print("-=" * 40)
print("cod ", end="")  # Título da coluna de código
for i in jogador.keys():  # Pega os nomes dos campos do último jogador cadastrado
    print(f"{i:<15} ", end="")  # Imprime os nomes dos campos formatados
print()

# Exibe os dados dos jogadores cadastrados
for k, v in enumerate(time):
    print(f"{k:>3} - ", end="")  # Mostra o código (índice) do jogador
    for d in v.values():  # Mostra os valores de cada campo do jogador
        print(f"{str(d):<15}", end="")
    print()

print("-=" * 40)

# Permite buscar os dados detalhados de um jogador específico
while True:
    buscar = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if buscar == 999:
        break  # Encerra a busca se digitar 999
    if buscar >= len(time):
        print(
            f"ERRO! Não existe jogador com código {buscar}!"
        )  # Verifica se o código é válido
    else:
        print(
            f"-- LEVANTAMENTO DO JOGADOR {time[buscar]['nome']}:"
        )  # Mostra nome do jogador selecionado
        for i, g in enumerate(time[buscar]["gols"]):
            print(f"    No jogo {i+1} fez {g} gols.")  # Mostra os gols por partida
    print("-" * 40)  # Separador visual

print("<< ENCERRADO >>")  # Mensagem final indicando o encerramento do programa
