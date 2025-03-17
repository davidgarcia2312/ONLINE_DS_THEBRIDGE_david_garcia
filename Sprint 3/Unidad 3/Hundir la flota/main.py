from funciones import menu_principal, turno_jugador, turno_maquina
from tablero import inicializar_tablero, generar_barcos_aleatorios
from variables import simbolo_barco


def jugar():

    registro_disparos_maquina = set()

    tablero_jugador = inicializar_tablero()
    tablero_maquina = inicializar_tablero()
    
    generar_barcos_aleatorios(tablero_jugador)
    generar_barcos_aleatorios(tablero_maquina)
    
    turno = True  # Comienza el jugador

    while True:
        if turno:
            turno = turno_jugador(tablero_jugador, tablero_maquina)
        else:
            turno = turno_maquina(tablero_jugador, registro_disparos_maquina)

        #Verificamos si alguien ganó
        if not (simbolo_barco in tablero_jugador):
            print("¡La máquina ha ganado!")
            break
        if not (simbolo_barco in tablero_maquina):
            print("¡Has ganado!")
            break


if __name__ == "__main__":
    if menu_principal():
        jugar()
