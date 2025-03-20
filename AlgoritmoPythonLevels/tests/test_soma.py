
# no terminal digitar:
# diretorio raiz: 
# cd C:\Users\ADM\WorkSpace\PythonCursoEmVideo\AlgoritmoPythonLevels

# pytest
# * se mudar o arquivo de diretorio, é preciso ajustar

# clicar em Run

import sys
import os
import pytest


# Adicionando a pasta 'src' ao path para importar corretamente os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.minha_funcao import soma  # Importação corrigida


def test_soma():
    assert soma(2, 3) == 5  # Teste passa
    assert soma(-1, 1) == 0  # Teste passa
    assert soma(0, 0) == 0  # Teste passa



