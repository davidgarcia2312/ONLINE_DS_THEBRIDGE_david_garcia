import numpy as np
import random
from variables import dim_tablero, barcos, simbolo_agua, simbolo_barco, simbolo_tocado, simbolo_agua_disparada


def inicializar_tablero():

    """Crea un tablero vacío"""

    return np.full((dim_tablero, dim_tablero), simbolo_agua)


def mostrar_tablero(tablero):

    """Muestra un tablero alineado correctamente en forma de cuadrícula"""

    for fila in tablero:
        print(" ".join(fila))  #Une los elementos con espacios para que se vean alineados
    print()  #Agrega una línea en blanco para mayor claridad


def mostrar_tablero_disparos(tablero_maquina):

    """Crea el tablero de disparos del usuario y lo muestra por pantalla (es decir, el tablero de la máquina sin revelar los barcos)"""

    tablero_disparos = np.where(tablero_maquina == simbolo_barco, simbolo_agua, tablero_maquina)
    print("\nTablero de disparos:")
    mostrar_tablero(tablero_disparos)


def colocar_barco(tablero, x, y, eslora, direccion):

    """
    Comprueba que se pueda colocar un barco de eslora y posición inicial dada en el tablero.
    x, y: Coordenadas iniciales
    eslora: Tamaño del barco
    direccion: 'N' (norte), 'S' (sur), 'E' (este) o 'O' (oeste)
    """

    if direccion == 'E':
        if (y + eslora - 1 > dim_tablero - 1) or (np.any(tablero[x, y:y+eslora] == simbolo_barco)):
            return False #Fuera del tablero o superpuesto
        else:
            tablero[x, y:y+eslora] = simbolo_barco
    elif direccion == 'O':
        if (y - eslora + 1 < 0) or (np.any(tablero[x, y-eslora+1:y+1] == simbolo_barco)):
            return False #Fuera del tablero o superpuesto
        else:    
            tablero[x, y-eslora+1:y+1] = simbolo_barco
    elif direccion == 'S':
        if (x + eslora - 1 > dim_tablero - 1) or (np.any(tablero[x:x+eslora, y] == simbolo_barco)):
            return False #Fuera del tablero o superpuesto
        else:
            tablero[x:x+eslora, y] = simbolo_barco
    elif direccion == 'N':
        if (x - eslora + 1 < 0) or (np.any(tablero[x-eslora+1:x+1, y] == simbolo_barco)):
            return False #Fuera del tablero o superpuesto
        else:
            tablero[x-eslora+1:x+1, y] = simbolo_barco
    return True  #Para registrar que se ha podido colocar el barco (si no se hubiese podido ya hubiésemos salido de la función en alguno de los return False)


def generar_barcos_aleatorios(tablero):

    """Coloca los barcos iniciales aleatoriamente en el tablero"""

    for longitud, cantidad in barcos.values():
        for _ in range(cantidad):
            colocado = False
            while not colocado:
                x = random.randint(0, dim_tablero - 1)
                y = random.randint(0, dim_tablero - 1)
                direccion = random.choice(['N', 'S', 'E', 'O'])
                colocado = colocar_barco(tablero, x, y, longitud, direccion)
    

def disparar_usuario(tablero_maquina, coordenada):

    """Registra un disparo en el tablero y cambia 'O' por 'X' si es un barco, o '~' por '-' si es agua"""

    if tablero_maquina[coordenada] == simbolo_barco:
        tablero_maquina[coordenada] = simbolo_tocado
        print("¡Tocado!\n")
        return True  #Para registrar que hemos impactado y seguir con el turno
    elif (tablero_maquina[coordenada] == simbolo_tocado) or (tablero_maquina[coordenada] == simbolo_agua_disparada):
        print("Ya has disparado aquí\n")
        return False  #Para registrar que hemos fallado y cambiar el turno
    else:
        tablero_maquina[coordenada] = simbolo_agua_disparada
        print("Agua\n")
        return False  #Para registrar que hemos fallado y cambiar el turno
    

def disparar_maquina(tablero_jugador, coordenada):

    """
    Funciona igual que disparar_usuario pero cambiando los mensajes que se muestran por pantalla y sin la condición de que se haya repetido disparo (pues ya lo evitamos utilizando el set en turno máquina)
    """

    if tablero_jugador[coordenada] == simbolo_barco:
        tablero_jugador[coordenada] = simbolo_tocado
        return True  #La máquina vuelve a disparar si impacta, igual que el usuario
    else:
        tablero_jugador[coordenada] = simbolo_agua_disparada
        return False  #Para indicar que falla y saltar de turno (o bien de turno interno o bien al del usuario)