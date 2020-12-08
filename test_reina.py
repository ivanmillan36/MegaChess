import pytest
from piezas.reina import getMovimientos
import tablero

BOARD_TEST_REINA =              (   '    P P P       ' +
                                    '                ' +
                                    '  P   q    P    ' +
                                    '                ' +
                                    '                ' +
                                    '   P  P  P      ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '   p  p  p      ' +
                                    '                ' +
                                    '                ' +
                                    ' p    Q     p   ' +
                                    '                ' +
                                    '    p p p       ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_REINA, 6, 2, [[6, 1], [6, 0], [7, 1], [8, 0], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [7, 3], [8, 4], [9, 5], [6, 3], [6, 4], [6, 5], [5, 3], [4, 4], [3, 5], [5, 2], [4, 2], [3, 2], [2, 2], [5, 1], [4, 0]]),
        (BOARD_TEST_REINA, 6, 12, [[6, 11], [6, 10], [6, 9], [7, 11], [8, 10], [9, 9], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 12], [7, 13], [8, 14], [6, 13], [6, 14], [5, 13], [4, 14], [5, 12], [4, 12], [3, 12], [2, 12], [1, 12], [5, 11], [4, 10], [3, 9]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected