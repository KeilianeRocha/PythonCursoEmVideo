# Módulos = > O Python vem básico
"""são incrementos que ajudam a executar acoes no py
módulos são bibliotecas que são importados para o py
usando o comando import
ex:
inport bebidas #> importa todas as bebidas
from bebida inport refri #> importa somente os refri na biblioteca bebidas"""

from math import hypot
from random import random

"from random import random"


"""
importando o múdulo com todas as bibliotecas
import math
num = int(input('Digita um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada no número {} é {:.1f}'.format(num,raiz))"""

"""
importando do múdulo somente a biblioteca que eu preciso SQRT
from math import sqrt
num = int(input('Digita um número: '))
raiz = sqrt(num)
print('A raiz quadrada no número {} é {:.1f}'.format(num,raiz))"""

"""import emoji
print(emoji.emojize("ola mundo :sunglasses:")) 

# A partir da versão 2.0.0 do módulo emoji, o parâmetro use_aliases=True foi removido. Agora, os aliases não são mais 
# suportados por padrão. Para corrigir o erro, você pode simplesmente remover o argumento use_aliases=True
"""

#Desafio 016
"""#Importando módulos
from math import trunc
n = float(input('Digite um número: '))
i = trunc(n)
print('o número {} tem sua porção inteira de {}'.format(n, i))
#Sem importar módulos
n = float(input('Digite um número: '))
print('o número {} tem sua porção inteira de {}'.format(n, int(n)))"""

#Desafio 017
"""#Importando módulos
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#Sem importar módulos
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""

#Desafio 018
"""#Importando módulos
import  math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin((math.radians(angulo)))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno =  math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
#Sem importar módulos
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin((radians(angulo)))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno =  cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))"""
#Desafio 019
"""#classe random, metodo choice
import random
n1 = str(input('Nome do aluno 1:'))
n2 = str(input('Nome do aluno 2:'))
n3 = str(input('Nome do aluno 3:'))
n4 = str(input('Nome do aluno 4:'))
lista = [n1, n2,n3,n4]
esc = random.choice(lista)
print('O aluno escolhido foi {}'.format(esc))"""

#Desafio 020
import random
n1 = str(input('Nome do 1º aluno:'))
n2 = str(input('Nome do 2º aluno:'))
n3 = str(input('Nome do 3º aluno:'))
n4 = str(input('Nome do 4º aluno:'))
lista = [n1, n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)

#Desafio 021


#Desafio 022


#Desafio 023


#Desafio 024


#Desafio 025


#Desafio 026


#Desafio 027


