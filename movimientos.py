import tablero
from piezas import peon, torre, rey, reina, caballo, alfil
import constantes
from simulacion import simularJugadasFuturas

def getMovimientos(board, pieza, x, y):
    if(pieza == 'p' or pieza == 'P'):
        return peon.getMovimientos(board, x, y)
    if(pieza == 'q' or pieza == 'Q'):
        return reina.getMovimientos(board, x, y)
    if(pieza == 'r' or pieza == 'R'):
        return torre.getMovimientos(board, x, y)
    if(pieza == 'b' or pieza == 'B'):
        return alfil.getMovimientos(board, x, y)
    if(pieza == 'h' or pieza == 'H'):
        return caballo.getMovimientos(board, x, y)
    if(pieza == 'k' or pieza == 'K'):
        return rey.getMovimientos(board, x, y)

def getPuntosPieza(pieza):
    if(pieza == 'p' or pieza == 'P'):
        return constantes.SCORE_PEON
    if(pieza == 'q' or pieza == 'Q'):
        return constantes.SCORE_REINA
    if(pieza == 'r' or pieza == 'R'):
        return constantes.SCORE_TORRE
    if(pieza == 'b' or pieza == 'B'):
        return constantes.SCORE_ALFIL
    if(pieza == 'h' or pieza == 'H'):
        return constantes.SCORE_CABALLO
    if(pieza == 'k' or pieza == 'K'):
        return constantes.SCORE_REY

def getPuntosPorMovimiento(board, pieza, movimiento):
    if (pieza == 'p'):
        if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
            return getPuntosPieza(pieza) + movimiento[1] + 100
    if (pieza == 'P'):
        if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
            return getPuntosPieza(pieza) + 12 - movimiento[1] + 100
    if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
        return getPuntosPieza(pieza)
    else:
        piezaEnemiga = tablero.getPieza(board, movimiento[0], movimiento[1])
        if(tablero.campoEnemigo(piezaEnemiga, movimiento[1])):
            return getPuntosPieza(tablero.getPieza(board, movimiento[0], movimiento[1])) * 100
        else:
            return getPuntosPieza(tablero.getPieza(board, movimiento[0], movimiento[1])) * 30

def getMejorMovimientoPieza(board, pieza,x ,y ,movimientos):
    highScore = -99999999
    mejorMovimiento = []
    colorPlayer = tablero.getColor(pieza)
    posicionInicial = [x,y]
    if (movimientos != []):
        for movimiento in movimientos:
            score = getPuntosPorMovimiento(board, pieza, movimiento)
            # evaluar futuros movimientos, lo cual sumaria o restaria score para asi evaluar la jugada con el mayor score final.
            movimientoCompleto = [posicionInicial, movimiento]
            if(colorPlayer != ' '):
                score = score + simularJugadasFuturas(board, colorPlayer, colorPlayer, movimientoCompleto, constantes.CANT_ITERACIONES, score)
            if(score > highScore):
                highScore = score
                mejorMovimiento = movimiento
    return mejorMovimiento

def getPiezasPorColor(board, color):
    piezas = []
    for y in range(16):
        for x in range(16):
            pieza = tablero.getPieza(board, x, y)
            if (tablero.getColor(pieza) == color):
                piezas.append([pieza,x,y])
    return piezas

def getMejorMovimiento(board, color):
    try:
        piezas = getPiezasPorColor(board, color)
        mejorMovimiento = []
        mayorPuntaje = -99999999
        puntaje = 0
        for pieza in piezas:
            x = pieza[1]
            y = pieza[2]
            posicionInicial = [x,y]
            movimientosPieza = getMovimientos(board, pieza[0], x, y)
            if(movimientosPieza != []):
                movimiento = getMejorMovimientoPieza(board, pieza[0], x, y, movimientosPieza)
                if(movimiento != []):
                    puntaje = getPuntosPorMovimiento(board, pieza[0], movimiento)
                    if(puntaje > mayorPuntaje):
                        mayorPuntaje = puntaje
                        mejorMovimiento = [posicionInicial,movimiento]
        return mejorMovimiento
    except:
        print("movimientos: Error al obtener mejor movimiento")


