"""
no terminal digitar:
.cd AlgoritmoPythonLevels/testesPytestpytest
pytest
ou so clicar em Run
"""

import pytest
from minha_funcao import (soma,)  # Supondo que a função esteja em um arquivo chamado minha_funcao.py


def test_soma():
    assert soma(2, 3) == 5  # Teste passa
    assert soma(-1, 1) == 0  # Teste passa
    assert soma(0, 0) == 0  # Teste passa


if __name__ == "__main__":
    pytest.main()



""" _ Expected_Result_

============================ test session starts =============================
collected 1 item                                                               
test_soma.py .                                                           [100%]

============================= 1 passed in X.XXs ==============================

"""
