# TODO: Crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
# Seu aplicativo devera analisar se a pexpressão passada esta como os parenteses abertos e fechados na ordem correta

# Inicializa uma pilha vazia para controle de parênteses
pilha = []

# Solicita a expressão matemática ao usuário
expr = str(input("Digite a expressão: "))

# Percorre cada símbolo da expressão
for simb in expr:
    # Se encontrar um abre parênteses, empilha
    if simb == "(":
        pilha.append("(")

    # Se encontrar um fecha parênteses
    elif simb == ")":
        # Verifica se há parênteses abertos para fechar (pilha não vazia)
        if len(pilha) > 0:
            pilha.pop()  # Remove o último '(' da pilha
        else:
            # Se não houver '(' para fechar, empilha ')' e interrompe
            pilha.append(")")
            break

# Ao final, verifica se todos os parênteses foram fechados corretamente
if len(pilha) == 0:
    print(f"Sua expressão está válida!")
else:
    print(f"Sua expressão está errada!")
