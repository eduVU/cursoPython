import time, os
import juego
import comunicacion as comm
import estadisticas as est

print("Iniciando BlackJack...")
time.sleep(1)
print("¡Bienvenido!\n")

interruptor = "ok"  # Variable que controla el bucle principal.

while True:
    # Menú para seleccionar usuarios.
    usuario, interruptor = comm.menu_usuarios()
    if interruptor == "salir": break  # Esto se activa si el jugador decide salir.
    
    # Menú para escoger opciones de jugador.
    interruptor = comm.menu_usuarios2(usuario)
    if interruptor == "salir": break  # Esto se activa si el jugador decide salir.

    # Se define si el juego tiene 1 o 2 jugadores.    
    modo_juego = input("Seleccione el modo de juego (solo/duo):")
    os.system("cls")

    # Se inicializan los nombres de los jugadores disponibles.
    if modo_juego.lower() == "solo": jugadores = [usuario]
    elif modo_juego.lower() == "duo": jugadores = [usuario, "Jugador2"]

    # Se crea el juego con 1 o 2 usuarios.
    partida = juego.Juego(jugadores)

    # Se muestran las cartas iniciales de cada jugador
    interruptor = partida.mostrar_estado_partida()
    if interruptor == "salir": continue  # Si algún jugador obtuvo una mano especial, gana y termina la partida.

    estados = []  # Estado de cada jugador (ganador/perdedor/otros)
    puntajes= []  # Puntaje de cada jugador

    # Se llevan a cabo los turnos de cada jugador.
    estados, puntajes, interruptor = partida.jugar_turno()
    if interruptor == "salir": continue  # Si algún jugador ganó por regla especial, termina la partida y vuelve al menú.

    # Si ambos jugadores perdieron, se declara al dealer como ganador.
    if estados.count("perdedor") == len(estados):
        print("¡El ganador es el dealer!\n")
        condicion = "Derrota"
        est.crear_estadisticas(usuario, condicion)
        continue

    # Se lleva a cabo el turno del dealer.
    estadoD, puntajeD, interruptor = partida.jugar_turno_dealer()
    if interruptor == "salir": continue  # Si el dealer ganó por regla especial, se termina la partida.

    # En caso de que nadie ganara por reglas especiales, se determina al ganador según su puntaje.
    else: partida.definir_ganador(usuario, estados, puntajes, estadoD, puntajeD)