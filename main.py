j1 = 'X'
j2 = 'O'
nj = '*'

def bienvenida():
    pass

def imprimir_tablero(tablero:"matriz"):
    pass

def cambiar_jugador(jugador:str) -> str:
    pass

def triqui(tablero:"matriz") -> bool:
    pass

def hacer_jugada(tablero:"matriz", jugador:str) -> "matriz":
    pass

def imprimir_ganador(tablero:"matriz"):
    pass

def main():
    bienvenida()
    jugador:str = nj
    tablero:"matriz" = [
        [nj, nj, nj],
        [nj, nj, nj],
        [nj, nj, nj]
    ]
    while not triqui(tablero):
        imprimir_tablero(tablero)
        jugador = cambiar_jugador(jugador)
        tablero = hacer_jugada(jugador, tablero)
    
    imprimir_ganador(tablero)

main()