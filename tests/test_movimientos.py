import pytest
import sys
sys.path.append("/home/ivanmillan36/Documentos/proyectos VSCode/MegaChess2/")
import constantes
import movimientos

@pytest.mark.parametrize(
    "board, color, expected",
    [
        (constantes.PLAYEER_TEST_MEJOR_MOVIMIENTO, 'black', [[1, 9], [1, 12]]),
    ] 
)
def test_getMejorMovimiento(board, color, expected):
    assert movimientos.getMejorMovimiento(board, color) == expected
