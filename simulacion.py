import tablero
from piezas import peon, torre, rey, reina, caballo, alfil
import constantes


def getMejorMovimiento(board, color):
    try:
        piezas = getPiezasPorColor(board, color)
        mejorMovimiento = []
        mayorPuntaje = 0
        puntaje = 0
        for pieza in piezas:
            x = pieza[1]
            y = pieza[2]
            posicionInicial = [x,y]
            movimiento = getMejorMovimientoPieza(board, pieza[0], getMovimientos(board, pieza[0], x, y))
            if(movimiento != []):
                puntaje = getPuntosPorMovimiento(board, pieza[0], movimiento)
                if(puntaje > mayorPuntaje):
                    mayorPuntaje = puntaje
                    mejorMovimiento = [posicionInicial,movimiento]
        return {'mejorMovimiento':mejorMovimiento, 'mayorPuntaje':mayorPuntaje}
    except:
        print("Simulacion: Error al obtener mejor movimiento")

def getPiezasPorColor(board, color):
    piezas = []
    for y in range(16):
        for x in range(16):
            pieza = tablero.getPieza(board, x, y)
            if (tablero.getColor(pieza) == color):
                piezas.append([pieza,x,y])
    return piezas

def getMejorMovimientoPieza(board, pieza, movimientos):
    try:
        highScore = 0
        mejorMovimiento = []
        if (movimientos != []):
            for movimiento in movimientos:
                score = getPuntosPorMovimiento(board, pieza, movimiento)
                if(score > highScore):
                    highScore = score
                    mejorMovimiento = movimiento
        return mejorMovimiento
    except:
        print("Simulacion: Error al obtener mejor movimiento de pieza.")

def getPuntosPorMovimiento(board, pieza, movimiento):
    try:
        if (pieza == 'p'):
            if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
                return getPuntosPieza(pieza) + movimiento[1] + 100
        if (pieza == 'P'):
            if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
                return getPuntosPieza(pieza) + 15 - movimiento[1] + 100
        if (tablero.posicionVacia(board, movimiento[0], movimiento[1])):
            return getPuntosPieza(pieza)
        else:
            piezaEnemiga = tablero.getPieza(board, movimiento[0], movimiento[1])
            if(tablero.campoEnemigo(piezaEnemiga, movimiento[1])):
                return getPuntosPieza(tablero.getPieza(board, movimiento[0], movimiento[1])) * 100
            else:
                return getPuntosPieza(tablero.getPieza(board, movimiento[0], movimiento[1])) * 30
    except:
        print("Simulacion: Error al obtener puntos por movimiento.")

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

def simularJugadasFuturas(board, colorSimulado, color, movimiento, iteraciones, score):
    try:
        iteracionesRestantes = iteraciones
        newBoard = tablero.getTableroLuegoDeMovimiento(board, movimiento)
        if (colorSimulado == 'black'):
            colorSimulado = 'white'
            Mejormovimiento = getMejorMovimiento(newBoard,colorSimulado)
        else:
            colorSimulado = 'black'
            Mejormovimiento = getMejorMovimiento(newBoard,colorSimulado)

        if(color != colorSimulado):
            newScore = score - Mejormovimiento['mayorPuntaje']
        else:
            newScore = score + Mejormovimiento['mayorPuntaje']

        iteracionesRestantes = iteraciones - 1
        if(iteracionesRestantes == 0):
            return newScore
        else:
            return simularJugadasFuturas(newBoard, colorSimulado, color, Mejormovimiento['mejorMovimiento'], iteracionesRestantes, newScore)
    except:
        return score

#score = simularJugadasFuturas(constantes.TABLERO_INICIAL, 'black', 'black', [[1,9],[1,10]], 20, 0)
#print(score)