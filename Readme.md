![icons8-python-150](https://github.com/KeilianeRocha/AlgoritmosComPython-/assets/109313933/d0bb8ba0-13e8-476e-8e0c-d9f29bedcdf4)

<h1 align="center"> Desafio de Programação Python </h1>
<p align="right">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO"/>
</p>

---

 # Algoritmo com Python

---
## Resumo

> "Um algoritmo é uma sequência de raciocínios, instruções ou operações para alcançar um objetivo, sendo necessário que os passos sejam finitos e operados sistematicamente. Um algoritmo, portanto, conta com a entrada `(input)` e saída `(output)` de informações mediadas pelas instruções." - [rockcontent](https://rockcontent.com/br/blog/algoritmo/#:~:text=Um%20algoritmo%20%C3%A9%20uma%20sequ%C3%AAncia,matem%C3%A1tico%20%C3%A1rabe%20do%20s%C3%A9culo%20IX.)

## Linguagem Python

- Python é uma linguagem de propósito geral, conhecida por sua simplicidade e versatilidade.
- Facilidade e intuição fazem parte da sua essência.
- Multiplataforma, organizada e orientada a objetos.
- Possui muitas bibliotecas que facilitam o desenvolvimento.

## Onde Aplicar?

- Inteligência Artificial
- Biotecnologia
- Computação 3D

## Instalação

1. O sistema operacional Windows não inclui o Python por padrão.
2. Baixe e instale o Python: [Python.org](https://www.python.org/)
3. Marque a opção "Add Path" durante a instalação.

Depois de instalado, confirme a instalação usando o seguinte comando no terminal:

```bash
python --version
```

## Iniciando no Python
- Utilize o IDLE como terminal interativo.
- IDLE: Função interativa para testar comandos.
- Script: Utilize para programar.

# Exemplo de Funções

## Imprime algo na tela
```Python
print('Olá, Mundo!')
```

## Lê uma entrada do usuário
````python
nome = input('Qual o seu nome? ')
print(nome)
````
# Teoria
- Delimitadores: Use 'aspas simples' ou "aspas duplas" para str.
- Comandos: Todo comando é uma função.
- Função: Toda função deve ter () ex: **print**.
- Mensagens devem está entre "string", números não são colocados entre "aspas"
- Variáveis: Espaços em memória que recebem valores.


# Formatando Texto

## Alinhamento à direita
````python
nome = input('Digite seu nome: ')
print('Olá {:>20}'.format(nome))
````
## Alinhamento à esquerda
````python
nome = input('Digite seu nome: ')
print('Olá {:<20}'.format(nome))
````
# Alinhamento centralizado
````python
nome = input('Digite seu nome: ')
print('Olá {:^20}'.format(nome))
````
# Tipos Primitivos
- int: Número inteiro (ex: 7, -4, 0, 9875)
- float: Número real (ex: 4.5, 0.076, -15.223, 7.0)
- bool: Valor lógico (True, False)
- str: Texto ('olá', "olá", '7,5', '')

# Operações Aritméticas
- +: Adição
- -: Subtração
- *: Multiplicação
- /: Divisão
- %: Módulo/resto da divisão
- **: Potência
- //: Divisão inteira

# Ordem de Precedência
- ()
- **
- *, /, //, %
- +, -

# Módulos em Python

- [Python.org](https://www.python.org/): Verifique a versão do Python no console do Python.
- [Python Docs](https://docs.python.org/): Consulte a referência de bibliotecas.
- [PyPI](https://pypi.org/): Explore pacotes adicionais.
- Python permite a criação de módulos para compartilhamento na comunidade.
- Programas Python, por padrão, têm comandos limitados, tornando a linguagem ágil.

## Comandos Básicos para Importar Módulos

- `import xxx`: Importa de forma generalista as funcionalidades do módulo.
- `from xxx import yyyy`: Importação otimizada para importar uma funcionalidade específica.
- Escrita: `módulo.variável` (Exemplo: `random.numero`).

# Manipulação de Cadeias de Texto

- Para o Python, toda cadeia de texto está em 'simples'.
- Índice: Cada espaço recebe um índice na cadeia de texto.
  - Exemplo: `frase = "curso de"`.
  - Índices: [0][1][2][3][4][5][6][7].

## Fatiamento de String

- `frase[2]`: Seleciona a letra no índice 2.
- `frase[2:6]`: Seleciona do índice 2 ao 5, eliminando o 6.
- `frase[2:8]`: Seleciona até o índice 7 (não é a melhor forma de fatiar).
- `frase[2:7:2]`: Seleciona pulando de 2 em 2.
- `frase[:5]`: Seleciona do 0 ao 4.
- `frase[5:]`: Seleciona do 5 até o final.
- `frase[5::3]`: Seleciona do 5 até o final de 3 em 3.

## Análise de String

- `len(frase)`: Mostra a quantidade de espaços na frase.
- `frase.count('o')+1`: Conta quantas vezes 'o' aparece na frase. 
  - E o `+1` evita que ela inicie no índice `0`
- `frase.find('deo')`: Busca a frase 'deo' e mostra em que momento ela começa.
- `'curso' in frase`: Verifica se 'curso' existe na frase.
- `frase.rfind('A')`: Busca a frase 'deo' e mostra em que momento ela termina.

## Transformação

- `frase.replace('curso', 'android')`: Procura e substitui.
- `frase.upper()`: Transforma em maiúsculo.
- `frase.capitalize()`: Coloca todos para minúsculo, deixando apenas a primeira letra em maiúsculo.
- `frase.title()`: Capitaliza as primeiras letras de cada palavra.
- `frase.strip()`: Remove espaços inúteis.
- `frase.rstrip()`: Remove espaços inúteis no final.
- `frase.lstrip()`: Remove espaços inúteis à esquerda.

## Divisão

- `frase.split()`: Divide a string considerando os espaços.

## Junção

- `'-'.join(frase)`: Junta a frase usando '-' como delimitador.
---

# Salvando e Executando
- Crie uma pasta no computador.
  - Abra o IDLE ou utilize um ambiente de desenvolvimento como o 
  [PyCharm - Community.](https://www.jetbrains.com/pycharm/download/other.html)
- Crie um arquivo dentro da pasta com extensão .py.
- Digite o código.
- Salve o arquivo e execute.
- **Mantenha seu código organizado**
---

# Estruturas de Controle
- `if.. elif.. else, for` e `while`

## Condições Aninhadas
Uma conidição dentro da outra.
### Exemplo

```Python
if carro.esquerda(): # Não esqueça os dois pontos`:`
#se carro.esquerda()
  carro.siga()
  carro.direita()
  carro.siga()
  carro.direita()
  carro.esquerda()
  carro.siga()
  carro.direita()
  carro.siga()
elif carro.direita(): # Em caso de mais de 3 condições, é possível adicionar quantos `elif` forem necessários. Nunca pode ser usado sem um `if`.
#senao se carro.direita()
  carro.siga()
  carro.esquerda()
  carro.siga()
  carro.esquerda()
  carro.siga()
else: # Pode ser sado nenhuma ou uma única vez
#senao
  carro.siga()
carro.para()
```

## Estruturas de repetição 'for'
- Também chamado de `laço de repetição - iteração`
- Estrutura de repetição com variável de controle *(quando se sabe o limite)*
```Python
for c in range(1,10): # laço c no intervalo(1,10)
  passo
pega
```
--
```Python
for c in range(0,3): # laço c no intervalo(0,3)
  passo
  pula
passo
pega
```
--
```Python
for c in range(0,3): # laço c no intervalo(0,3)
  if moeda # se moeda, pega e segue a repetição
    pega
  passo
  pula
passo
pega
```

## Estruturas de repetição 'while'
- Estrutura de repetição com teste lógico
```Python
while not apple: # Se não maçã (não determina o quantitativo de passos ate a maçã)
  passo
pega # encerra os passos
```
--
```Python
while not apple:
  if chao
  ande
  if buraco:
    pule 
  if moeda:
    pega
pega
```

### Break
- 
```Python
while True: # True → é um loop infinito
  if chao
  ande
  if buraco:
    pula 
  if moeda:
    pega
  if troféu
    pula
    Break  # O comando Break faz com que haja a saída do laço de repetição
           # evita que apos pegar o treféu ele retorne para um laço infinito
pega
```

## Variaveis Compostas `tuplas()`
- Com ou sem `()`
- Podem armazenar vários valores (definir a quantidade)
- Existem no Python 3 tipos:
  - `Tuplas`
  - `Listas`
  - `Dicionário`
- Utiliza indices para localizar cada valor `[var0][var1]`...
- Pode usar:
  - Método `len()` **comprimento** → quantos elementos tem dentro da variável
  - Estruturas de repetição
  ### Limitação: 
    **As `tuplas ` são imutáveis** 
      - Entretanto é possível apagar a variável usando → `del(var)`*mas não pode apagar um único elemento*

```Python
loja = 'Mouse', 'Monitor', 'Teclado', 'MousePad'
print = (f' Itens em estoque'{loja})
```
--

#### Formas de usar `tuplas` com for
```Python
loja = 'Mouse', 'Monitor', 'Teclado', 'MousePad'
for item in loja:
    print(f' - {item}')
print(f'\nTotal de itens em estoque: {len(loja)}')
```

#### Aceita dados de tipos diferentes dentro da `tuplas`
P. ex.:

```Python
pessoa = ('Aline', 39, 'M', 65.5)
print(pessoa)
```
## Variaveis Compostas `listas[]`
- Podem se mutáveis → o elemento rocado é eliminado
- Para adicionar novo item → usa o método `var.append['newvar']`
- Adicionar um novo item em determinada posição → `var.insert[0,'newvar']`
- Formas de eliminar itens
  - `del var[varnum]` → Remove por índice
  - `var.pop[var]` → indicado o índice a excluir `var.pop[]` → usado pra eliminar o último índice
  - `var.remove['var']` → não remove por índice e sim por conteúdo
  - **Após a remoção do ítem, os demais são realinhados.**
- Para verificar se um item esta na lista:
```python
if'a' in vogais: # o operador in é bem importante nas estruturas compostas
  vogais.remove['x'] # so vou remover o item, se ele estiver na lista
```
- Algumas formas de manipular índices 
  - Criar listas por meio de `range` → `var = list[range(4,11)]`
  - Ordenar valores em uma `list` → `var.sort[]`
  - Inverter ordem → `var.sort[reverse=True]`
  - Para saber o tamanho de uma `list` → `len[var]`
#### Listas dentro de listas (compostas)

## Variaveis Compostas `dicionarios{}`
> Semelhante as 'tuplas()' e as 'listas[]', so que é possível ter indices literais p. ex.
>[0] → {nome}, [1] → {idade}

``` python

dados dict()
dados  {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
print(dados.values()) # pega todos os valores
print(dados.keys()) # pega so a marcação dos itens (nome, idade)
print(dados.items()) # pega ambos
```
´del´ → eleimina dados
´copy´ → método usado para fazer uma cópia semelhante ao [:]em listas

## Funções `def`
#### Função → um bloco de código reutilizável
    # outra vantagem: organização.

#### Estrutura de uma função

#### como funciona:
```Python
    def nome_da_funcao(parametros):
      # instrucao 1
      # instrucao 2
      # ...
      # return valor (opcional) → saida
```
---
Ex. de funções '`print()`, `len()` entre outras
Se eu quiser mostrar um linha na tela posso criar uma função pra isso p. ex.: `mostrarLinha()`
- Vantagem: evita linhas repetitivas, otimiza rotinas *Não é um laço!. Ele cria comandos personalizados, parametros
```python
# Função semparametro

def mostrarLinhas():
# 1
# 2
  # Entre a 'def' e o programa principal precisa existir 2 linhas de separação
  print("_______________________________________________")
mostraLinha() # toda vez que eu quiser que a 'def' seja executada, eu camo ela
print("xpts")
```
-- 
```python
# Função com parametro

def mensagem(msg):
  print("_______________________________________________")
  print(msg) # toda vez que eu quiser que a 'def' seja executada, eu camo ela
  print("_______________________________________________")
mensagem("Sistema de alunos")

```
# Interactive Help `help()`
Duas formas de chamar o comando
1- no terminal digite `help()` + a informação que deseja obter
p.ex.: `len`
para sair digite `quit`
2 - digite no arquivo.py p. ex.:
```Python
help(print) # mostra as infomações solicitadas
print(input.__doc__)
```
# Docstring
Manual de ajuda
```Python
def contador(i,f,p): # dentro da função
    """_docstring_
    -> faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    função criada por Keila
    """
    c = i
    while c <= f:
        print(f"{c}", end=' ')
        c += p
    print("Fim!")

# contador(2,10,2)

help(contador)
```
# Argumentos opcionais
Permite que o parametro seja opcional
```Python
def somar(a, b, c=0) # o uso de =0 indica que é opcional setar um valor para o
# argumento e `c` fica como ZERO
s = a + b + c
print(f"A somar vale {s}")
somar(2, 6)# dessa forma ele soma somente 2,6 e c como ZERO
```
# Escopo de variáveis
Local e Global
```Python
def teste()
x = 8
print(f"Na função teste, n vale {n}")
print(f"Na função teste, x vale {x}")


# Prigrama principal
n = 2 # mesmo estando fora da variavel local, não havera erro, pois trata-se de
# uma variavel global
  print(f"No programa principal, n vale {n}")
 teste()
 print(f"No programa principal, x vale {x}") # vai gerar erro pois X esta setado
 # somente na variavel local, antes do programa principal
```
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

# Retorno de resultados `return`
```Python
def somar(a, b=0, c=0)
s = a + b + c
return s

r1 = somar(2, 6)
r2 = somar(2, 6, 5)
r3 = somar(2)
# retorna um print personalizado
print(f"Meus resultados deram {r1},{r2},{r3}.")
```
min 50:04








---
***Em construção ...***



 
