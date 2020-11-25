import sys
sys.path.append("/home/ivanmillan36/Documentos/proyectos VSCode/MegaChess2/")
import tablero
import constantes

def getMovimientos(board, x, y):
    posicionInicial = [x,y]
    pieza = tablero.getPieza(board, x, y)
    color = tablero.getColor(pieza)
    movimientosPosibles = []

    if(color == 'black'):
        #eje y-
        X = x
        Y = y
        while(Y > 0):
            Y -= 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y-x+
        X = x
        Y = y
        while(Y > 0 and X < 15):
            Y -= 1
            X += 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje x+
        X = x
        Y = y
        while(X < 15):
            X += 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y+x+
        X = x
        Y = y
        while(Y < 15 and X < 15):
            Y += 1
            X += 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y+
        X = x
        Y = y
        while(Y < 15):
            Y += 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y+x-
        X = x
        Y = y
        while(Y < 15 and X > 0):
            Y += 1
            X -= 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje x-
        X = x
        Y = y
        while(X > 0):
            X -= 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y-x-
        X = x
        Y = y
        while(Y > 0 and X > 0):
            Y -= 1
            X -= 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                movimientosPosibles.append([X,Y])
                break



    if(color == 'white'):
        #eje y-
        X = x
        Y = y
        while(Y > 0):
            Y -= 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y-x+
        X = x
        Y = y
        while(Y > 0 and X < 15):
            Y -= 1
            X += 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje x+
        X = x
        Y = y
        while(X < 15):
            X += 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y+x+
        X = x
        Y = y
        while(Y < 15 and X < 15):
            Y += 1
            X += 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y+
        X = x
        Y = y
        while(Y < 15):
            Y += 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y+x-
        X = x
        Y = y
        while(Y < 15 and X > 0):
            Y += 1
            X -= 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje x-
        X = x
        Y = y
        while(X > 0):
            X -= 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                movimientosPosibles.append([X,Y])
                break
        
        #eje y-x-
        X = x
        Y = y
        while(Y > 0 and X > 0):
            Y -= 1
            X -= 1
            if (tablero.posicionVacia(board, X, Y)):
                movimientosPosibles.append([X,Y])
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
                break
            elif(tablero.getColor(tablero.getPieza(board, X, Y)) == 'black'):
                movimientosPosibles.append([X,Y])
                break

    return movimientosPosibles
