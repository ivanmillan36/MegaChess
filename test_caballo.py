import pytest
from piezas.caballo import getMovimientos
import tablero

BOARD_TEST_CABALLO =               ('                ' +
                                    '   P P          ' +
                                    '                ' +
                                    '    h           ' +
                                    '                ' +
                                    '   P P          ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '     h          ' +
                                    '                ' +
                                    '  p p           ' +
                                    '            H   ' +
                                    '   H            ' +
                                    '                ' +
                                    '  p p           ' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_CABALLO, 4, 3, [[5, 1], [6, 2], [6, 4], [5, 5], [3, 5], [2, 4], [2, 2], [3, 1]]),
        (BOARD_TEST_CABALLO, 5, 9, [[6, 7], [7, 8], [7, 10], [6, 11], [3, 10], [3, 8], [4, 7]]),
        (BOARD_TEST_CABALLO, 12, 12, [[13, 10], [14, 11], [14, 13], [13, 14], [11, 14], [10, 13], [10, 11], [11, 10]]),
        (BOARD_TEST_CABALLO, 3, 13, [[4, 11], [5, 12], [5, 14], [4, 15], [2, 15], [1, 14], [1, 12], [2, 11]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    print(getMovimientos(board, x,y))
    assert getMovimientos(board, x,y) == expected