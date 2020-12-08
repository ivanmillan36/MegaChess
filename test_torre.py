import pytest
from piezas.torre import getMovimientos
import tablero

BOARD_TEST_TORRE =               (  '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    ' P              ' +
                                    '                ' +
                                    'Pr   P          ' +
                                    '            p   ' +
                                    '                ' +
                                    ' P      p   R  p' +
                                    '                ' +
                                    '                ' +
                                    '            p   ' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_TORRE, 1, 9, [[1, 8], [1, 7], [2, 9], [3, 9], [4, 9], [5, 9], [1, 10], [1, 11], [1, 12], [0, 9]]),
        (BOARD_TEST_TORRE, 12, 12, [[12, 11], [12, 10], [13, 12], [14, 12], [15, 12], [12, 13], [12, 14], [12, 15], [11, 12], [10, 12], [9, 12], [8, 12]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected