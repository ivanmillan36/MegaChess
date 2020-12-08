import pytest
import movimientos
import constantes

PLAYEER_TEST_MEJOR_MOVIMIENTO = (   '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '     Q pppp     ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '       P P      ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '    BB          ' +
                                    '                ' +
                                    '       Kq       ' )

@pytest.mark.parametrize(
    "board, color, expected",
    [
        (PLAYEER_TEST_MEJOR_MOVIMIENTO, 'white', [[7, 15], [8, 15]]),
    ] 
)
def test_getMejorMovimiento(board, color, expected):
    assert movimientos.getMejorMovimiento(board, color) == expected

##############################################################################################

TEST_GET_MOVIMIENTOS_ENTRADA =  (   '      KqK       ' +
                                    '      KKK       ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, pieza, x, y, expected",
    [
        (TEST_GET_MOVIMIENTOS_ENTRADA,'q', 7 , 0, [[6,0], [6,1], [7,1], [8,1], [8,0]]),
    ] 
)
def test_getMovimientos(board, pieza, x, y, expected):
    movimientosObtenidos = movimientos.getMovimientos(board, pieza, x, y)
    succes = True
    for movimiento in expected:
        if(movimientosObtenidos.__contains__(movimiento) == False):
            succes = False
    assert succes == True

##############################################################################################

@pytest.mark.parametrize(
    "pieza, expected",
    [
        ('p', constantes.SCORE_PEON),
        ('q', constantes.SCORE_REINA),
        ('b', constantes.SCORE_ALFIL),
        ('h', constantes.SCORE_CABALLO),
        ('k', constantes.SCORE_REY),
        ('r', constantes.SCORE_TORRE),
        ('P', constantes.SCORE_PEON),
        ('Q', constantes.SCORE_REINA),
        ('B', constantes.SCORE_ALFIL),
        ('H', constantes.SCORE_CABALLO),
        ('K', constantes.SCORE_REY),
        ('R', constantes.SCORE_TORRE),
    ] 
)
def test_getPuntosPieza(pieza, expected):
    assert movimientos.getPuntosPieza(pieza) == expected


##############################################################################################

TEST_GET_PUNTOS_POR_MOVIMIENTO =  ( '       q        ' +
                                    '       K        ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, pieza, movimiento, expected",
    [
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'q', [7,1],  constantes.SCORE_REY*1000),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'K', [7,0],  constantes.SCORE_REINA*0),      
    ] 
)
def test_getPuntosPorMovimiento(board, pieza, movimiento, expected):
    assert movimientos.getPuntosPorMovimiento(board, pieza, movimiento) == expected