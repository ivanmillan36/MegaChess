import tablero

def getMovimientos(board, x, y):
    posicionInicial = [x,y]
    pieza = tablero.getPieza(board, x, y)
    color = tablero.getColor(pieza)
    movimientosPosibles = []

    if(color == 'black'):
        #cuadrante 1 1º
        X = x
        Y = y
        
        Y -= 2
        X += 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X,Y])

        
        #cuadrante 1 2º
        X = x
        Y = y
        
        Y -= 1
        X += 2
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 2 1º
        X = x
        Y = y
        
        Y += 1
        X += 2
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 2 2º
        X = x
        Y = y
        
        Y += 2
        X += 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 3 1º
        X = x
        Y = y
        
        Y += 2
        X -= 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 3 2º
        X = x
        Y = y
        
        Y += 1
        X -= 2
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 4 1º
        X = x
        Y = y
        
        Y -= 1
        X -= 2
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 4 2º
        X = x
        Y = y
        
        Y -= 2
        X -= 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X,Y])
        
    



    if(color == 'white'):
        #cuadrante 1 1º
        X = x
        Y = y
        
        Y -= 2
        X += 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
            movimientosPosibles.append([X,Y])

        
        #cuadrante 1 2º
        X = x
        Y = y
        
        Y -= 1
        X += 2
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 2 1º
        X = x
        Y = y
        
        Y += 1
        X += 2
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 2 2º
        X = x
        Y = y
        
        Y += 2
        X += 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 3 1º
        X = x
        Y = y
        
        Y += 2
        X -= 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 3 2º
        X = x
        Y = y
        
        Y += 1
        X -= 2
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 4 1º
        X = x
        Y = y
        
        Y -= 1
        X -= 2
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
            movimientosPosibles.append([X,Y])
        
        #cuadrante 4 2º
        X = x
        Y = y
        
        Y -= 2
        X -= 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X,Y])
        elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
            movimientosPosibles.append([X,Y])
    
    return movimientosPosibles