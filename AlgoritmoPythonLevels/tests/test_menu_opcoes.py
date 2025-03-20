# no terminal digitar:
# diretorio raiz:
# cd C:\Users\ADM\WorkSpace\PythonCursoEmVideo\AlgoritmoPythonLevels

# pytest
# * se mudar o arquivo de diretorio, é preciso ajustar

# clicar em Ru

import sys
import os
import pytest

# Adicionando a pasta 'src' ao path para importar corretamente os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.menu_opcoes import somar, multiplicar, maior


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 5) == 0

def test_maior():
    assert maior(2, 3) == 3
    assert maior(-1, 1) == 1
    assert maior(5, 5) == 5
