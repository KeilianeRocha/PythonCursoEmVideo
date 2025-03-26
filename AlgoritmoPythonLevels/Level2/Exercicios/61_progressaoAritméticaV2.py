# TODO: Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.


print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print("=" * 30)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

# Inicializa o contador e o termo atual
contador = 1  # Começa em 1 para exibir exatamente 10 termos
termo = primeiro

while contador <= 10 :
    print(termo, end=" → ") # alt + 26 pra fazer a setinha '_'
    termo += razao  # Calcula o próximo termo
    # formar simplificada de termo = termo + razao
    contador += 1  # Incrementa o contador

print("Acabou!")

"""
    o numero - contador → mostra resultado
    adiciona mais um numero → mostra add
    """