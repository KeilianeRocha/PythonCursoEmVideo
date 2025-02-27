# Condições
"""
Estruturas condicionais
'SE' BLOCO VERDADEIRO = True === if: ESTRUTURA SIMPLES
OU
'SENAO' BLOCO FALSO = False === else: ESTRUTURAS COMPLEXAS

--
EX: 

CONDIÇÃO SIMPLIFICADA
tempo = int(input("Quantos anos tem o seu carro?"))
print("Carro novo"if tempo <= 3 else "Carro velho")
print("--FIM--")

-- 

"""
tempo = int(input("Quantos anos tem o seu carro?"))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

