# operadores precisam de operandos (binarios)
# + => adição
# - => subtração
# * => multiplicação
# / => divisão flutuante
# // => divisão inteira
# % => módulo ou resto da divisão
# == => recebe
# ** => potencia
#from Exercicios.calculadoraV2 import subtracao, multiplicacao, divisao

# ordem de precedencia
#1. () no py para expressoes numericas so se usa o ()
#2. **
#3. * / // %
#4. + -

#Desafio 005
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
mult = n1 * n2

print('a soma é {} \na subtracão é {} \nmultiplicação é {}'.format(n1, n2, s, sub, mult))



