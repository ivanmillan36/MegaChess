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
            puntos = getPuntosPieza(pieza) + movimiento[1] + 100
            if(movimiento[0] == 0 or movimiento[0] == 1 or movimiento[0] == 14 or movimiento[0] == 15):
                puntos += 10
            return puntos
    if (pieza == 'P'):
        if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
            puntos = getPuntosPieza(pieza) + 15 - movimiento[1] + 100
            if(movimiento[0] == 0 or movimiento[0] == 1 or movimiento[0] == 14 or movimiento[0] == 15):
                puntos += 10
            return puntos
    if (pieza == 'q'):
        if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
            puntos = getPuntosPieza(pieza)
            if(movimiento[1] == 10):
                puntos += 200
                return puntos
    if (pieza == 'Q'):
        if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
            puntos = getPuntosPieza(pieza)
            if(movimiento[1] == 5):
                puntos += 200
                return puntos

    if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
        return getPuntosPieza(pieza)
    else:
        piezaEnemiga = tablero.getPieza(board, movimiento[0], movimiento[1])
        if(tablero.campoEnemigo(piezaEnemiga, movimiento[1])):
            return getPuntosPieza(piezaEnemiga) * 100
        else:
            if(movimiento[1] == 5 or movimiento[1] == 6 or movimiento[1] == 7 or movimiento[1] == 8 or movimiento[1] == 9 or movimiento[1] == 10):
                return getPuntosPieza(piezaEnemiga) * 1000
            else:
                return getPuntosPieza(piezaEnemiga) * 100

def getMejorMovimientoPieza(board, pieza,x ,y ,movimientos):
    highScore = -999999
    mejorMovimiento = []
    colorPlayer = tablero.getColor(pieza)
    posicionInicial = [x,y]
    if (movimientos != []):
        for movimiento in movimientos:
            score = getPuntosPorMovimiento(board, pieza, movimiento)
            # evaluar futuros movimientos, lo cual sumaria o restaria score para asi evaluar la jugada con el mayor score final.
            movimientoCompleto = [posicionInicial, movimiento]
            scoreSimulado = simularJugadasFuturas(board, colorPlayer, colorPlayer, movimientoCompleto, constantes.CANT_ITERACIONES, score)
            score = score + scoreSimulado
            if(score > highScore):
                highScore = score
                mejorMovimiento = movimiento
    return {'mejorMovimiento':mejorMovimiento, 'mayorPuntaje':highScore}

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
        mayorPuntaje = -999999
        puntaje = 0
        for pieza in piezas:
            x = pieza[1]
            y = pieza[2]
            posicionInicial = [x,y]
            movimientosPieza = getMovimientos(board, pieza[0], x, y)
            if(movimientosPieza != []):
                movimiento = getMejorMovimientoPieza(board, pieza[0], x, y, movimientosPieza)
                if(movimiento['mejorMovimiento'] != []):
                    puntaje = movimiento['mayorPuntaje']
                    if(puntaje > mayorPuntaje):
                        mayorPuntaje = puntaje
                        mejorMovimiento = [posicionInicial,movimiento['mejorMovimiento']]
        return mejorMovimiento
    except:
        print("movimientos: Error al obtener mejor movimiento")


