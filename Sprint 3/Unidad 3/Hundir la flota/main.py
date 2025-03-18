from funciones import menu_principal, turno_jugador, turno_maquina
from tablero import inicializar_tablero, generar_barcos_aleatorios
from variables import simbolo_barco


def jugar(dificultad_maquina):

    """
    Desarrollo completo del juego con los módulos ya creados
    """

    #Set vacío al que iremos añadiendo los disparos de la máquina para que no los repita (pues se generan aleatorios, podría pasar)
    registro_disparos_maquina = set() 

    #Inicializamos los tableros con los barcos para el usuario y para la máquina
    tablero_jugador = inicializar_tablero()
    tablero_maquina = inicializar_tablero()
    generar_barcos_aleatorios(tablero_jugador)
    generar_barcos_aleatorios(tablero_maquina)
    
    turno = True  #Comienza el usuario

    while True:

        #Aquí gestionamos los cambios de turno con el booleano que devuelven turno_jugador y turno_maquina(véanse las funciones en el módulo correspondiente)
        if turno:
            turno = turno_jugador(tablero_jugador, tablero_maquina)
        else:
            turno = turno_maquina(tablero_jugador, registro_disparos_maquina, dificultad_maquina)

        #Verificamos si alguien ganó
        if not (simbolo_barco in tablero_jugador):
            print("¡La máquina ha ganado!")
            break
        if not (simbolo_barco in tablero_maquina):
            print("¡Has ganado!")
            break


#Este bloque asegura que el juego solo se ejecute si este script se ejecuta directamente
#y no si se importa como un módulo en otro archivo (se incluye para hacer todo más robusto)
if __name__ == "__main__":
    dificultad = menu_principal()  #Recogemos la dificultad elegida
    if dificultad: #Si se ha recogido un valor dificultad si o si es 1,2 o 3, que siempre devuelve True
        jugar(dificultad)  #Se pasa la dificultad a jugar()
