# TODO: Escreva um programa para aprovar o espréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# TODO: Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negaado.

casa = float(input("Qual o valor da casa R$"))
salario = float(input("Qual o valor do seu salário R$ "))
anos = int(input("Em quantos anos você pretende pagar? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(
    f"Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}"
)

if prestacao <= minimo:
    print(f" Emprestimo APROVADO!")
else:
    print("Emprestimo NEGADO!")

print(f"{'Fim do Programa ':=^30}")
