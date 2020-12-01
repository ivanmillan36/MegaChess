import pytest
import movimientos

PLAYEER_TEST_MEJOR_MOVIMIENTO = (   '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    ' q              ' +
                                    '                ' +
                                    '                ' +
                                    ' P              ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, color, expected",
    [
        (PLAYEER_TEST_MEJOR_MOVIMIENTO, 'black', [[1, 9], [1, 12]]),
    ] 
)
def test_getMejorMovimiento(board, color, expected):
    assert movimientos.getMejorMovimiento(board, color) == expected
