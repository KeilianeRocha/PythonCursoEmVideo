# TODO: Faça um programa que leia nome e média de um aluno, quardando também a 
# situação em um dicionário. No final, mostre o conteúdo fa estrutura na tela.

# Reprovado → Menor que 5,0
# Aprovado → IGUAL 7,0
# Recuperação → Menor ou Igual a 6,0


aluno = {}  # OK – Dicionário criado

aluno["nome"] = str(input("Nome: ")
).capitalize()  # OK – Nome com a primeira letra maiúscula
aluno["nota"] = []  # OK – Lista de notas

for c in range(1, 5):
    nota = float(input(f"Nota {c}: "))
    aluno["nota"].append(nota)  # OK – Notas armazenadas corretamente

media = sum(aluno["nota"]) / len(aluno["nota"])  # OK – Média calculada corretamente
aluno["media"] = media  # OK – Média armazenada no dicionário

print(f"Média: {aluno['media']}")  # OK – Exibe a média

# Análise da situação:
if media >= 7:
    aluno["situação"] = "Aprovado"
    # print(f"Aluno(a): {aluno['nome']}\nMédia: {aluno['media']}\nSituação: 
    # APROVADO")  # OK – Situação "Passou" para >= 7.0
elif 5 <= media < 7:
    aluno["situação"] = "Recuperação"
    # print(f"Aluno(a): {aluno['nome']}\nMédia: {aluno['media']}\nSituação: 
    # RECUPERAÇÃO")  # OK – Situação "Reprovou" para < 6.0
else:
    aluno["situação"] = "Reprovado"
    # print(f"Aluno(a): {aluno['nome']}\nMédia: {aluno['media']}\nSituação: 
    # REPROVADO")  # OK – Situação "Recuperação" para == 6.0
print("\n== RESULTADO FINAL ==")
for chave, valor in aluno.items(): # percorre todos os dados do dicionário 
    # (nome, notas, média, situação)
    print(f"{chave.capitalize()}: {valor}")
