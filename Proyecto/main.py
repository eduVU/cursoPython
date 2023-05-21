import time, clases
import manejo_usuarios as usuarios
import comunicacion as comm
import os

puntos = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Esta función cuenta los puntos en la mano del jugador.
def calcular_puntaje(jugador):
    puntaje = 0
    # Se calcula el puntaje según la mano del jugador.
    for i in range(len(jugador.mano)):
        puntaje = puntaje + puntos.get(jugador.mano[i].valor)
    return puntaje

def evaluar_jugador(jugador):
    estado = ""
    puntaje = calcular_puntaje(jugador)
    if puntaje > 21:
        print(f"Tu puntaje es {puntaje}, ¡perdiste!")
        estado = "perdedor"
        time.sleep(1)
    elif puntaje == 21:
        print(f"Tu puntaje es {puntaje}, ¡ganaste!")
        estado = "ganador"
        time.sleep(1)
    else: estado = "jugando"
    return estado, puntaje

def evaluar_dealer(dealer):
    estado = ""
    puntaje = calcular_puntaje(dealer)
    if puntaje > 21:
        print(f"El puntaje del dealer es {puntaje}, ¡el dealer pierde!")
        estado = "perdedor"
        time.sleep(1)
    elif puntaje == 21:
        print(f"El puntaje del dealer es {puntaje}, ¡El dealer gana!")
        estado = "ganador"
        time.sleep(1)
    elif puntaje < 18: 
        mazo.repartir(dealer)
        estado = "jugando"
        time.sleep(1)
    else: estado = "listo"
    return estado, puntaje


# Se evalúan las condiciones de la partida para elegir un ganador.
def definir_ganador(estado1, estado2, estadoD="", puntaje1=0, puntaje2=0, puntajeD=0):
    # Si algún participante perdió, su puntuación no se considera al determinar al jugador con más puntos.
    if estadoD == "perdedor": puntajeD = 0
    if estado1 == "perdedor": puntaje1 = 0
    if estado2 == "perdedor": puntaje2 = 0
    
    punt_max = max(puntaje1, puntaje2, puntajeD)

    # Se determina al ganador o si hay empate basado en el máximo puntaje.
    if puntaje1 == punt_max and estado1 != "perdedor": 
        if puntaje1 == puntaje2:
            if puntaje1 == puntajeD: print("¡Empate triple!")
            else: print("¡Empate entre ambos jugadores!.")
        elif puntaje1 == puntajeD: print("¡Empate entre el Jugador1 y el dealer!.")
        else: print(f"¡El ganador es Jugador1! con {puntaje1} puntos")
    elif puntaje2 == punt_max and estado2 != "perdedor":
        if puntaje2 == puntajeD: print("¡Empate entre el Jugador2 y el dealer.")
        else: print(f"¡El ganador es Jugador2 con {puntaje2} puntos!")
    else: print(f"¡El ganador es el dealer con {puntajeD} puntos!")
    # print(estado1,estado2,estadoD)
    # print(puntaje1,puntaje2,puntajeD)

# TO DO: 
# ajustar los métodos de Juego()
# evaluar los puntos al mostrar estado del juego
# revelar la mano del dealer cuando gana/pierde

# Estructura:
# 1. Iniciar el programa -- DONE
# 2. Definir los usuarios
# 3. Pasar los usuarios a Juego(), iniciar el juego. 
#---------------------------- ESTO SERÁ EL MAIN ----------------------------
print("Iniciando BlackJack...")
time.sleep(1)
print("¡Bienvenido!\n")

interruptor = "ok"

while True:
    # Este menú seleciona el usuario.
    menu_usuarios = int(input("Ingrese una opción:\n"
                      "1. Crear un usuario nuevo.\n"
                      "2. Usar un usuario existente.\n"
                      "3. Salir.\n"))
    os.system("cls")

    if menu_usuarios == 1:    
        usuario, interruptor = usuarios.crear_usuario()
        if interruptor == "salir": continue
    elif menu_usuarios == 2:
        usuario, interruptor = usuarios.escoger_usuario()
        if interruptor == "salir": continue
    elif menu_usuarios == 3: print("¡Adios!"); break
    else: continue

    # # Este menú selecciona las acciones para el usuario elegido.
    # menu_jugador = int(input("Ingrese una opción:\n"
    #                   "1. Nueva partida.\n"
    #                   "2. Ver estadísticas.\n"
    #                   "3. Salir.\n"))
    # os.system("cls")

    # if menu_jugador == 2:
    #     ver_estadisticas(usuario)

    # XXXXXXXXX- INTEGRAR ESTE BLOQUE EN JUEGO -XXXXXXXXXXXX
    # Se genera un nuevo mazo y se baraja.
    mazo = clases.Baraja()
    mazo.barajar()

    # n = int(input("Ingrese el número de jugadores :"))
    # Se inicia la partida con dos jugadores y el dealer.
    jugador1 = clases.Mano()
    jugador2 = clases.Mano()
    dealer = clases.Mano()

    # Se reparten las cartas iniciales.
    mazo.repartir(jugador1,inicial=True)
    mazo.repartir(jugador2,inicial=True)
    mazo.repartir(dealer,inicial=True)

    #-------- ESTADO DE LA PARTIDA -------.
    print("------------------\n"
          "Estado de la partida.\n")
    
    print("------------------\n"
          "Jugador1.\n")
    jugador1.mostrar_cartas()
    
    print("------------------\n"
          "Jugador2.\n")
    jugador2.mostrar_cartas()
    
    print("------------------\n"
          "Dealer.\n")
    dealer.mostrar_cartas(modo="dealer")
    time.sleep(1)
    
    # XXXXXXXXX- INTEGRAR ESTE BLOQUE EN JUEGO -XXXXXXXXXXXX

    #-------- TURNO DEL JUGADOR 1 --------.
    print("------------------\n"
            "Turno de Jugador1.\n")

    # Convertir en una función --> nuevo modulo "menu.py(?)"
    while True:
        # Se muestra la mano actual del jugador.
        jugador1.mostrar_cartas()

        # Se evalúa si el jugador ganó, perdió o sigue jugando normalmente con base en los puntos en su mano.
        estado1, puntaje1 = evaluar_jugador(jugador1)

        if estado1 == "perdedor": break  # Si el jugador perdió, termina el turno.
        elif estado1 == "ganador": interruptor = "salir"; break  # Si el jugador ganó, termina la partida.

        # Este menú permite al usuario decidir qué hacer en la partida. -----> Convertir en una función.
        menu2 = int(input("¿Qué desea hacer?\n"
                        "1. Pedir una carta.\n"
                        "2. Terminar el turno.\n"))
        
        if menu2 == 1: mazo.repartir(jugador1)
        else: break

    if interruptor == "salir": continue

    #-------- TURNO DEL JUGADOR 2 --------.
    print("------------------\n"
            "Turno de Jugador2.\n")

    while True:
        jugador2.mostrar_cartas()
        estado2, puntaje2 = evaluar_jugador(jugador2)
        
        if estado2 == "perdedor": break
        elif estado2 == "ganador": interruptor = "salir"; break

        menu2 = int(input("¿Qué desea hacer?\n"
                        "1. Pedir una carta.\n"
                        "2. Pasar el turno.\n"))
        
        if menu2 == 1: mazo.repartir(jugador2)
        else: break

    if interruptor == "salir": continue

    # En este caso, se declara al ganador sabiendo que ambos jugadores ya perdieron.
    if estado1 == "perdedor" and estado2 == "perdedor": print("¡El ganador es el dealer!"); continue

    #-------- TURNO DEL DEALER --------.
    print("------------------\n"
            "Turno del Dealer.\n")

    while True:
        dealer.mostrar_cartas()#modo="dealer")
        estadoD, puntajeD = evaluar_dealer(dealer)

        if estadoD == "perdedor": break
        elif estadoD == "ganador": interruptor = "salir"; break
        elif estadoD == "jugando": continue
        else: break

    if interruptor == "salir": continue
    else: definir_ganador(estado1,estado2,estadoD,puntaje1,puntaje2,puntajeD)
    """ 
    estado1 = ""
    puntaje1 = 20

    estado2 = "perdedor"
    puntaje2 = 29

    estadoD = "perdedor"
    puntajeD = 28
    """