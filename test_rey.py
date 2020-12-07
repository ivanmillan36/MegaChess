import pytest
from piezas.rey import getMovimientos
import tablero

BOARD_TEST_REY =               (    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    ' k              ' +
                                    '                ' +
                                    '                ' +
                                    '            K   ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_REY, 1, 9, [[1, 8], [2, 8], [2, 9], [2, 10], [1, 10], [0, 10], [0, 9], [0, 8]]),
        (BOARD_TEST_REY, 12, 12, [[12, 11], [13, 11], [13, 12], [13, 13], [12, 13], [11, 13], [11, 12], [11, 11]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected