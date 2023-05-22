import time
import juego
import comunicacion as comm
import estadisticas as est

# TO DO: 
# Ajustar la asignación de puntos para el As.
# Agregar las reglas adicionales de victoria (5 menores, blackjack, etc.)

print("Iniciando BlackJack...")
time.sleep(1)
print("¡Bienvenido!\n")

interruptor = "ok"  # Variable que controla el bucle principal.

while True:
    # Menú para seleccionar usuarios.
    usuario, interruptor = comm.menu_usuarios()
    if interruptor == "salir": break
    
    # Menú para escoger opciones de jugador.
    interruptor = comm.menu_usuarios2(usuario)
    if interruptor == "salir": break

    # Se define si el juego tiene 1 o 2 jugadores.    
    modo_juego = input("Seleccione el modo de juego (solo/duo):")

    # Se inicializan los nombres de los jugadores disponibles.
    if modo_juego.lower() == "solo": jugadores = [usuario]
    else: jugadores = [usuario, "Jugador2"]

    # Se crea el juego con 1 o 2 usuarios.
    este_juego = juego.Juego(jugadores)

    # Se muestran las cartas iniciales de cada jugador
    este_juego.mostrar_estado_partida()

    # Se llevan a cabo los turnos de cada jugador.
    estados = []  # Estado de cada jugador (ganador/perdedor)
    puntajes= []  # Puntaje de cada jugador

    for i in range(len(jugadores)):
        print("------------------\n"
              f"Turno de {jugadores[i]}.\n")
        while True:
            # Se muestra la mano actual del jugador.
            este_juego.manos_jugadores[i].mostrar_cartas()

            # Se evalúa si el jugador ganó, perdió o sigue jugando normalmente con base en los puntos de su mano.
            estado, puntaje = este_juego.evaluar_jugador(este_juego.manos_jugadores[i])
            estados.append(estado); puntajes.append(puntaje)
            if estado == "perdedor": break  # Si el jugador perdió, termina el turno.
            elif estado == "ganador": interruptor = "salir"; break  # Si el jugador ganó, termina la partida.

            # Este menú permite al usuario decidir qué hacer en la partida.
            menu_turno = int(input("¿Qué desea hacer?\n"
                            "1. Pedir una carta.\n"
                            "2. Terminar el turno.\n"))
            
            if menu_turno == 1: este_juego.mazo.repartir(este_juego.manos_jugadores[i])
            else: break
        if interruptor == "salir": continue  # Si el jugador ganó, termina la partida.

    # Si ambos jugadores perdieron, se declara al dealer como ganador.
    if estados.count("perdedor") == len(estados):
        print("¡El ganador es el dealer!")
        condicion = "Derrota"
        est.crear_estadisticas(usuario, condicion)
        continue

    # Se lleva a cabo el turno del dealer.
    print("------------------\n"
          "Turno del Dealer.\n")
    while True:
        este_juego.dealer.mostrar_cartas(modo="dealer")
        estadoD, puntajeD = este_juego.evaluar_dealer()
        estados.append(estadoD); puntajes.append(puntajeD)
        if estadoD == "perdedor": break
        elif estadoD == "ganador": interruptor = "salir"; break
        elif estadoD == "jugando": continue
        else: break
    if interruptor == "salir": continue  # Si el dealer ganó, se termina la partida.
    else:
        # Si a este punto nadie ganó por llegar a 21, se determina el ganador comparando los puntos.
        este_juego.definir_ganador(usuario, estados, puntajes)
 