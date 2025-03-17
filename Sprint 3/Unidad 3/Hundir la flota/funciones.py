import random
import textwrap
from tablero import disparar_usuario, disparar_maquina, mostrar_tablero_disparos, mostrar_tablero
from variables import dim_tablero


def menu_principal():

    """
    Despliega un menú principal sencillo que se muestra al ejecutar el módulo principal
    """

    while True:

        print("\n--- HUNDIR LA FLOTA ---")
        print("1. Jugar")
        print("2. Información")
        print("3. Salir del juego")

        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            return True
        elif opcion == "2":
            texto = """\
            Esto es una simplificación del clásico hundir la flota.
            Jugarás contra la máquina y el objetivo es hundir todos sus barcos antes de que hunda los tuyos.
            En cada turno podrás darme las coordenadas donde quieras disparar y también comprobar cuáles han sido tus disparos.
            Si aciertas, sigues disparando, sino, le tocará a la máquina. Puedes salir del juego en cualquier momento.
            ¡SUERTE!
            """
            print(textwrap.dedent(texto))
        elif opcion == "3":
            print("Saliendo del juego...")
            return False
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def turno_jugador(tablero_jugador, tablero_maquina):

    """
    Desarrolla el turno del jugador, desplegando un menú con 4 opciones diferentes
    """

    print("\nTu turno. Opciones:")
    print("1. Disparar")
    print("2. Mostrar tablero de disparos")
    print("3. Mostrar mi tablero")
    print("4. Salir del juego")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        x = int(input("Introduce la fila (0-9): "))
        y = int(input("Introduce la columna (0-9): "))
        if not disparar_usuario(tablero_maquina, (x,y)):
            return False  #Cambiamos el turno si fallamos el disparo

    elif opcion == "2":
        mostrar_tablero_disparos(tablero_maquina)

    elif opcion == "3":
        print("\nTu tablero actual:")
        mostrar_tablero(tablero_jugador)  #Para ver cómo va la máquina

    elif opcion == "4":
        print("Saliendo del juego...")
        exit()

    return True  #Mantenemos turno si no se disparó (por ejemplo, si hemos elegido mostrar uno de los tableros)


def turno_maquina(tablero_jugador, registro_disparos_maquina):

    """
    Función más sencilla que desarrolla el turno de la máquina, que es aleatorio, internamente.
    No permite que la máquina repita disparo y muestra si nos ha impactado o no.
    """

    print("\nTurno de la máquina.")

    while True:
        #Generamos una coordenada aleatoria que no haya sido disparada antes
        while True:
            x = random.randint(0, dim_tablero - 1)
            y = random.randint(0, dim_tablero - 1)
            if (x, y) not in registro_disparos_maquina:
                break

        registro_disparos_maquina.add((x, y))  #Guardamos el disparo de la máquina en el set para no repetirlo después

        #La máquina dispara, si falla devuelve False y pasa el turno al jugador
        cambia_turno = disparar_maquina(tablero_jugador,(x,y))
        if not cambia_turno:
            return True


