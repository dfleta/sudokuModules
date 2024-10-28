import pytest
from src.checkCuadrado import checkCuadrado
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("sudoku, sano",
                         [  (casosTest.correct, True),
                            (casosTest.incorrect, True),
                            (casosTest.incorrect1, True),
                            (casosTest.incorrect2, True),
                            (casosTest.incorrect3, True),
                            (casosTest.incorrect4, True),
                            (casosTest.incorrect5, True),
                            (casosTest.irregular, False),
                            (casosTest.irregular2, False)])
def test_sudoku_valido(sudoku, sano):
    assert checkCuadrado(sudoku) == sano
