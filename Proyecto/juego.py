import time
import deck
import estadisticas as est

# Diccionario con puntaje para cada carta dentro del juego según su valor.
puntos = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class Juego():
    def __init__(self, jugadores):
        # Diccionario con puntaje para cada carta dentro del juego según su valor.
        self.puntos = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                       '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        
        # Baraja del juego
        self.mazo = deck.Baraja()
        self.mazo.barajar() # Siempre se mezcla la baraja.

        # Se definen los nombres de los jugadores del juego.
        self.nombres_usuario = jugadores

        # Se crea una mano para cada jugador en la partida y para el dealer.
        self.manos_jugadores = []
        for nombre in self.nombres_usuario:
            nombre = deck.Mano()
            self.manos_jugadores.append(nombre)
        
        self.dealer = deck.Mano()

        # Se reparte una mano inicial a cada jugador y al dealer.
        for mano in self.manos_jugadores:
            self.mazo.repartir(mano, inicial=True)

        self.mazo.repartir(self.dealer, inicial=True)

    # Se muestran las cartas iniciales y se consulta si algún jugador tiene un puntaje ganador.
    def mostrar_estado_partida(self):   
        print("------------------\n"
              "Estado de la partida.\n")      
        
        for i in range(len(self.nombres_usuario)):
            print("------------------\n")
            self.manos_jugadores[i].mostrar_cartas(self.nombres_usuario[i])
            self.evaluar_jugador(self.manos_jugadores[i])
             
        print("------------------\n"
              "Dealer.\n")
        self.dealer.mostrar_cartas("", modo="dealer")
        self.evaluar_dealer(modo="oculto")

        time.sleep(1)

    # Esta función cuenta los puntos en la mano del jugador.
    def calcular_puntaje(self, jugador):
        puntaje = 0
        # Se calcula el puntaje según la mano del jugador.
        for i in range(len(jugador.mano)):
            puntaje = puntaje + puntos.get(jugador.mano[i].valor)
        return puntaje

    # Esta función comprueba el estado de la partida para ccada jugador según su puntaje.
    def evaluar_jugador(self, jugador):
        estado = ""
        puntaje = self.calcular_puntaje(jugador)
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

    # Esta función comprueba el estado de la partida para el dealer y toma acciones según su puntaje actual.
    def evaluar_dealer(self, modo="revelar"):
        estado = ""
        puntaje = self.calcular_puntaje(self.dealer)
        if puntaje > 21:
            if modo == "revelar": self.dealer.mostrar_cartas()
            print(f"El puntaje del dealer es {puntaje}, ¡el dealer pierde!")
            estado = "perdedor"
            time.sleep(1)
        elif puntaje == 21:
            if modo == "revelar": self.dealer.mostrar_cartas()
            print(f"El puntaje del dealer es {puntaje}, ¡El dealer gana!")
            estado = "ganador"
            time.sleep(1)
        elif puntaje < 18: 
            self.mazo.repartir(self.dealer)
            estado = "jugando"
            time.sleep(1)
        else: 
            estado = "listo"
            if modo == "revelar": self.dealer.mostrar_cartas()
        return estado, puntaje

    # Se evalúan las condiciones de la partida para elegir un ganador.
    def definir_ganador(usuario, estados, puntajes):
        # Escenario cuando no hay jugador 2.
        if len(estados) == 2:
            estado1 = estados[0]; estadoD = estados[1]; estado2 = "perdedor"
            puntaje1 = puntajes[0]; puntajeD = puntajes[1]
        else:
            estado1 = estados[0]; estado2 = estados[1]; estadoD = estados[2]
            puntaje1 = puntajes[0]; puntaje2 = puntajes[1]; puntajeD = puntajes[2]
               
        # Si algún participante perdió, su puntuación no se considera al determinar al jugador con más puntos.
        if estadoD == "perdedor": puntajeD = 0
        if estado1 == "perdedor": puntaje1 = 0
        if estado2 == "perdedor": puntaje2 = 0
        
        punt_max = max(puntaje1, puntaje2, puntajeD)

        # Se determina al ganador o si hay empate basado en el máximo puntaje.
        condicion = "Derrota"
        if puntaje1 == punt_max and estado1 != "perdedor": 
            if puntaje1 == puntaje2:
                if puntaje1 == puntajeD: 
                    print("¡Empate triple!")
                    condicion = "Empate"
                else: 
                    print("¡Empate entre ambos jugadores!.")
                    condicion = "Empate"
            elif puntaje1 == puntajeD: 
                print("¡Empate entre el Jugador1 y el dealer!.")
                condicion = "Empate"
            else: 
                print(f"¡El ganador es Jugador1! con {puntaje1} puntos")
                condicion = "Victoria"
        elif puntaje2 == punt_max and estado2 != "perdedor":
            if puntaje2 == puntajeD: print("¡Empate entre el Jugador2 y el dealer.")
            else: print(f"¡El ganador es Jugador2 con {puntaje2} puntos!")
        else: print(f"¡El ganador es el dealer con {puntajeD} puntos!")

        # Se guardan los resultados de la partida en el registro del jugador.
        est.crear_estadisticas(usuario, condicion)