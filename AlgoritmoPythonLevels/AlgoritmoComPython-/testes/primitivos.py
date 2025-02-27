#variaveis
"""#print('hello word')
age = 20
first_name = 'Ada'
is_online = False #Boolean value neeb be in CaspLock
print(age,first_name )"""

#input
"""name = input('what is your name? ')
print('hello ' + name)"""

#date
"""birth_year = input('enter your birth year: ')
age = 2024 - int(birth_year)
print(age)"""

#int 7 -4 0 9875
"""first = input('First: ')
second = input('Second: ')
sum = int(first) + int(second)
print(sum)"""

#float 4.5 0.076 -15.223 7.0
"""first = float(input('First: '))
second = float(input('Second: '))
sum = first + second
print('sum: ' + str(sum))"""

# boolean True False
"""recive True or False, value neeb be in CaspLock"""

#String or str 'olá' '7.5' or "olá" '7.5' or '' ""
"""all caracteres and they need be between "" or '' """

course = 'python for beginners'
print(course.upper())

 #------------------------------x------------------------------------#

#Desafio 002
"""n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
#print(" A soma vale", s)
print('a soma entre {} e {} vale {}'.format(n1, n2, s))"""

#Desafio 003
"""n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
print('a soma entre {} e {} é {}!'.format(n1,n2, s))"""

#Desafio 004
"""p = (input("Digite algo"))
print("o tipo primitivo desse valor é ",type(p))
print('so tem espaço',p.isspace())
print('é um número?',p.isnumeric())
print('é alfabetico?',p.isalpha())
print('esta em maiúscula',p.isupper())
print('esta em munuscula?',p.islower())
print("esta capitalizado?",p.istitle())"""

#Desafio 005
"""n = int(input('digite um número: '))
#s = n1 - 1
#sum = n1 + 1
# quando vc usar variaveis, menos memoria vc gasta

print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n,(n-1), (n+1) ))"""

#Desafio 006
"""n = int(input('digite um número: '))
print('O dobro de {} vale {} \nO triplo de {} é {}\nE a raiz quadrada de {} é {:.2f}'
      .format(n, (n * 2),n,(n*3), n, (n ** (1/2))))"""

#Desafio 007 (variaveis de py aceitam acento)
"""n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
print('A média entre {} e {} é igual a {:.1f}'.format(n1, n2,((n1+n2)/2)))"""

#Desafio 008
"""d = float(input('digite uma distancia em metros: '))
print('A medida de {} coresponde a \n'
      '{}cm\n'
      '{}mm'.format(d,(d * 100), d,(d * 1000)))"""

#Desafio 009
"""print('-'*12, 'TABUADA', '-'*12)
n = int(input("Digite um número"))
print('{} x 1 = {}\n'
      '{} x 2 = {}\n'
      '{} x 3 = {}\n'
      '{} x 4 = {}\n'
      '{} x 5 = {}\n'
      '{} x 6 = {}\n'
      '{} x 7 = {}\n'
      '{} x 8 = {}\n'
      '{} x 9 = {}\n'
      '{} x 10 = {}\n'.format(n, (n *1), n, (n *2),n, (n *3), n, (n *4),n, (n *5),n, (n *6),n, (n *7),n, (n *8),
                            n, (n *9),n, (n *10)))
print('-'*12, 'FIM DO PROGRAMA')"""

#Desafio 010
"""r = float(input('Quanto dinheiro você tem na carteira? R$ '))
coverter = r / 3.27
print('Com R${} você pode comprar US${:.1f}'.format(r, coverter))"""

#Desafio 011
"""larg = float(input('largura da parede:'))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua area é de {}m².'.format(larg, alt, area))
tinta  = area / 2
print('Para pintar essa parede, você vai precisar de {}l de tinta.'.format(tinta))"""

#Desafio 012
"""preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))"""

#Desafio 013
"""funcionario = float(input('Digite o valor do Salário do Fincionário: R$ '))
novoSalario = funcionario + (funcionario * 15 / 100)
print('O funcionário recebia R${}, com o acressímo de 15% o salário atual dele é de R${} '.format(funcionario,
                                                                                                  novoSalario))"""
#Desafio 014
"""c = float(input('Informe a temperatura em: Cº'))
f = ((9*c)/5) + 32 #=> mesmo sem os parênteses a ordem de precedência seria seguida
#Utilizamos a fórmula TC/5 = (TF – 32)/9, em que TC é temperatura
# em graus Celsius e TF é temperatura em Fahrenheit.
print('A temperatura de {}Cº corresponde a {}ºF!'.format(c,f))"""

#Desafio 015
"""dias = float(input('Quantos dias alugados? ')) # cada dia é R$60.00
km = float(input('Quantos Km rodados?')) # cada km é R$ 0,15
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))"""


