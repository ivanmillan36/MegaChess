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
        (PLAYEER_TEST_MEJOR_MOVIMIENTO, 'black', [[8, 15], [7, 15]]),
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
                                    '       R        ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, pieza, x, y, expected",
    [
        (TEST_GET_MOVIMIENTOS_ENTRADA,'q', 7 , 0, [[6,0], [6,1], [7,1], [8,1], [8,0]]),
        (TEST_GET_MOVIMIENTOS_ENTRADA,'R', 7 , 11, [[7, 10], [7, 9], [7, 8], [7, 7], [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [8, 11], [9, 11], [10, 11], [11, 11], [12, 11], [13, 11], [14, 11], [15, 11], [7, 12], [7, 13], [7, 14], [7, 15], [6, 11], [5, 11], [4, 11], [3, 11], [2, 11], [1, 11], [0, 11]]),
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

TEST_GET_PUNTOS_POR_MOVIMIENTO =  ( 'pk     q        ' +
                                    '       K        ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    'q               ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    'P               ' )

@pytest.mark.parametrize(
    "board, pieza, movimiento, expected",
    [
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'q', [7,1],  constantes.SCORE_REY*1000),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'q', [1,8],  constantes.SCORE_REINA +100),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'q', [0,9],  constantes.SCORE_REINA),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'K', [7,0],  constantes.SCORE_REY*0),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'k', [1,1],  100),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'p', [0,1],  constantes.SCORE_PEON+1+100),      
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'P', [0,14],  constantes.SCORE_PEON+15-14+100),
    ] 
)
def test_getPuntosPorMovimiento(board, pieza, movimiento, expected):
    assert movimientos.getPuntosPorMovimiento(board, pieza, movimiento) == expected