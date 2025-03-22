# TODO: Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.


print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print("=" * 30)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))


# Inicializa o contador e o termo atual
contador = 1  # Começa em 1 para exibir exatamente 10 termos
termo = primeiro
total = 0
mais = 10

while mais != 0 :
    total += mais # cintas os termos + novos termos 'mais'
    while contador <= total:
        print(termo, end=" → ")
        termo += razao  # Calcula o próximo termo
        contador += 1  # Incrementa o contador
    print("Pause")
    mais = int(input("Quantos termos você quer adicionar a mais? "))  
    print(f"Progresão finalizada com {total} termos")
