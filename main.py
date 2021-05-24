j1 = 'X'
j2 = 'O'
nj = '*'

def bienvenida():
    print("Bienvenido al mejor triqui de consola del mundo mundial")
    print("Este juego esta diseñado para 2 jugadores asi que levantate", end= ' ') 
    print("y trae a uno de tus amigos ahora mismo (si es que tienes alguno)")

def imprimir_tablero(tablero:"matriz"):
    for fila in tablero:
        for elemento in fila:
            print(elemento, end='\t')
        print()

def cambiar_jugador(jugador:str) -> str:
    if jugador == j1:
        return j2
    else:
        return j1

def triqui(tablero:"matriz") -> bool:
    if tablero[0][0] != nj and tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return True
    elif tablero[0][2] != nj and tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return True
    elif tablero[0][0] != nj and tablero[0][0] == tablero[1][0] == tablero[2][0]:
        return True
    elif tablero[0][1] != nj and tablero[0][1] == tablero[1][1] == tablero[2][1]:
        return True
    elif tablero[0][2] != nj and tablero[0][2] == tablero[1][2] == tablero[2][2]:
        return True
    elif tablero[0][0] != nj and tablero[0][0] == tablero[0][1] == tablero[0][2]:
        return True
    elif tablero[1][0] != nj and tablero[1][0] == tablero[1][1] == tablero[1][2]:
        return True
    elif tablero[2][0] != nj and tablero[2][0] == tablero[2][1] == tablero[2][2]:
        return True
    else:
        return False

def tablero_lleno(tablero:"matriz") -> bool:
    for fila in tablero:
        for elemento in fila:
            if elemento == nj:
                return False
    return True

def jugada_valida(x:str, fila:int, columna:int) -> bool:
    return x == nj and 0 <= fila < 3 and 0 <= columna < 3

def hacer_jugada(tablero:"matriz", jugador:str) -> "matriz":
    jugada = False
    while jugada == False:
      fila = int(input("Ingrese la fila: ")) - 1
      columna = int(input("Ingrese la columna: ")) - 1
      x = tablero[fila][columna]
      if jugada_valida(x, fila, columna):
        tablero[fila][columna] = jugador
        jugada = True
      else:
        print("Jugada invalida")
    return tablero

def imprimir_ganador(tablero:"matriz", jugador:str):
    imprimir_tablero(tablero)
    if triqui(tablero):
        if jugador == j1:
            print("Gano el jugador 1")
        elif jugador == j2:
            print("Gano el jugador 2")
    elif tablero_lleno(tablero):
        print("Empate")

def main():
    bienvenida()
    jugador:str = nj
    tablero:"matriz" = [
        [nj, nj, nj],
        [nj, nj, nj],
        [nj, nj, nj]
    ]
    while not (triqui(tablero) or tablero_lleno(tablero)):
        imprimir_tablero(tablero)
        jugador = cambiar_jugador(jugador)
        tablero = hacer_jugada(tablero, jugador)
    
    imprimir_ganador(tablero, jugador)

main()