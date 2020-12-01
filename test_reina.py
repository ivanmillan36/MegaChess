import pytest
from piezas.reina import getMovimientos
import tablero

BOARD_TEST_REINA =              (   'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'p pppppppppppppp' +
                                    ' q ppppppppppppp' +
                                    'p pppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_REINA, 1, 9, [[1, 8], [2, 9], [1, 10], [0, 9]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected