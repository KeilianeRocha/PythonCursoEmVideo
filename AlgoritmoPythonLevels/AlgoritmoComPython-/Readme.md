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
***Em construção ...***



 
