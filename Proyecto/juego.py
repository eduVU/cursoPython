import time
import deck
import estadisticas as est

class Juego():
    def __init__(self, jugadores):
        # Diccionario con puntaje para cada carta dentro del juego según su valor.
        self.puntos = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                       '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        
        # Baraja del juego.
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
        interruptor = "ok"
        estados = []
        puntajes = []
        print("------------------\n"
              "Estado de la partida.\n")      
        for i in range(len(self.nombres_usuario)):
            print("------------------\n")
            self.manos_jugadores[i].mostrar_cartas(self.nombres_usuario[i])
            estado, puntaje = self.evaluar_jugador(self.manos_jugadores[i])
            estados.append(estado); puntajes.append(puntaje)          
        print("------------------\n"
              "Dealer.\n")
        self.dealer.mostrar_cartas("", modo="dealer")
        estadoD, puntajeD = self.evaluar_dealer(modo="oculto")
        
        if "ganador" in estados or estadoD == "ganador":
            interruptor = "salir"
            self.definir_ganador(self.nombres_usuario[0], estados, puntajes, estadoD, puntajeD)
        return interruptor

    # Esta función cuenta los puntos en la mano del jugador y las condiciones especiales de victoria.
    # El valor por defecto del As es 11.
    def calcular_puntaje(self, jugador):
        regla = "normal"
        puntaje = 0
        lista_valores = []  # Almacena los valores de las cartas que tiene el jugador en la mano.
        lista_menores = []  # Almacena los valores de las cartas menores a 10.
        # Se calcula el puntaje de la mano del jugador.
        for i in range(len(jugador.mano)):
            valor = jugador.mano[i].valor
            lista_valores.append(valor)
            if self.puntos.get(valor) < 10 or valor == "A": lista_menores.append(valor)
            puntaje = puntaje + self.puntos.get(valor)

        # Se comprueba si el jugador tiene un Blackjack: 2 cartas y 21 puntos.
        if len(lista_valores) == 2  and puntaje == 21:
            regla = "Blackjack"
            return puntaje, regla

        # Se define si el As debe valer 1 o 11 ajustando el puntaje.
        conteo_ases = lista_valores.count("A")  # Contar la cantidad de ases totales.    
        for i in range(conteo_ases):
            if puntaje <= 21: # Mientras el puntaje sea válido no modifica nada.
                break
            else:
                puntaje -= 10 # Se considera cada As como uno hasta que el puntaje < 21.
        
        # Se comprueba si el jugador consiguió 5 menores.
        if puntaje <= 21 and len(lista_menores) >= 5:
            regla = "cinco menores"
            return puntaje, regla
        
        # Se comprueba si el jugador tiene tres 7's.
        if puntaje <= 21 and lista_menores.count("7") == 3:
            regla = "tres 7's"
            return puntaje, regla
        return puntaje, regla

    # Esta función comprueba el estado de la partida para ccada jugador según su puntaje.
    def evaluar_jugador(self, jugador):
        estado = ""
        puntaje, regla = self.calcular_puntaje(jugador)
        if regla == "Blackjack":
            print(f"Obtuviste un {regla}, ¡ganaste!\n")
            estado = "ganador"
            time.sleep(1)
        elif regla == "cinco menores":
            print(f"Obtuviste {regla}, ¡ganaste!\n")
            estado = "ganador"
            time.sleep(1)
        elif regla == "tres 7's":
            print(f"Obtuviste {regla}, ¡ganaste!\n")
            estado = "ganador"
            time.sleep(1)
        if puntaje > 21:
            print(f"Tu puntaje es {puntaje}, ¡perdiste!\n")
            estado = "perdedor"
            time.sleep(1)
        else: estado = "jugando"
        return estado, puntaje

    # Esta función comprueba el estado de la partida para el dealer y toma acciones según su puntaje actual.
    def evaluar_dealer(self, modo="revelar"):
        estado = ""
        puntaje, regla = self.calcular_puntaje(self.dealer)
        if regla == "Blackjack":
            self.dealer.mostrar_cartas("Dealer")  # Se revela la mano completa del dealer.
            print(f"El dealer obtuvo un {regla}, ¡el dealer gana!\n")
            estado = "ganador"
            time.sleep(1)
        elif regla == "cinco menores":
            self.dealer.mostrar_cartas("Dealer")
            print(f"El dealer obtuvo {regla}, ¡el dealer gana!\n")
            estado = "ganador"
            time.sleep(1)
        elif regla == "tres 7's":
            self.dealer.mostrar_cartas("Dealer")
            print(f"El dealer obtuvo {regla}, ¡el dealer gana!\n")
            estado = "ganador"
            time.sleep(1)
        elif puntaje > 21:
            self.dealer.mostrar_cartas("Dealer")
            print(f"El dealer tiene {puntaje} puntos, ¡el dealer pierde!\n")
            estado = "perdedor"
            time.sleep(1)
        elif puntaje < 17: 
            self.mazo.repartir(self.dealer)
            estado = "jugando"
            time.sleep(1)
        else: 
            estado = "listo"
            if modo == "revelar": self.dealer.mostrar_cartas("Dealer")
        return estado, puntaje
    
    # Determina el estado dentro de la partida y puntaje para cada jugador.
    def jugar_turno(self):
        estados = []  # Estado de cada jugador (ganador/perdedor)
        puntajes= []  # Puntaje de cada jugador
        interruptor = "ok"
        for i in range(len(self.nombres_usuario)):
            if interruptor == "salir": continue
            print("------------------\n"
                f"Turno de {self.nombres_usuario[i]}.\n")
            while True:
                # Se muestra la mano actual del jugador.
                self.manos_jugadores[i].mostrar_cartas(self.nombres_usuario[i])

                # Se evalúa si el jugador ganó, perdió o sigue jugando normalmente con base en los puntos de su mano.
                estado, puntaje = self.evaluar_jugador(self.manos_jugadores[i])
                
                # Si el jugador perdió, se documenta el resultado y termina el turno.
                if estado == "perdedor":
                    estados.append(estado); puntajes.append(puntaje)
                    break 
                # Si el jugador ganó, termina la partida y se registra la victoria. 
                elif estado == "ganador": 
                    interruptor = "salir"
                    if self.nombres_usuario[i] == "Jugador2": condicion = "Derrota"
                    else: condicion = "Victoria"
                    est.crear_estadisticas(self.nombres_usuario[0], condicion)
                    break

                # Este menú permite al usuario decidir qué hacer en la partida.
                menu_turno = int(input("¿Qué desea hacer?\n"
                                "1. Pedir una carta.\n"
                                "2. Terminar el turno.\n"))
                print("\n")
                if menu_turno == 1: self.mazo.repartir(self.manos_jugadores[i])
                else:
                    estados.append(estado); puntajes.append(puntaje); break
        return estados, puntajes, interruptor

    # Determina el estado dentro de la partida y puntaje para el dealer.
    def jugar_turno_dealer(self):
        interruptor = "ok"
        print("------------------\n"
              "Turno del Dealer.\n")
        while True:
            self.dealer.mostrar_cartas("", modo="dealer")
            estado, puntaje = self.evaluar_dealer()
            if estado == "perdedor": 
                return estado, puntaje, interruptor; break
            elif estado == "ganador": 
                condicion = "Derrota"; interruptor = "salir"
                est.crear_estadisticas(self.nombres_usuario[0], condicion)
                return estado, puntaje, interruptor; break
            elif estado == "jugando": continue
            else: return estado, puntaje, interruptor; break

    # Se evalúan las condiciones de la partida para elegir un ganador.
    def definir_ganador(self, usuario, estados, puntajes, estadoD, puntajeD):
        # Escenario cuando no hay jugador 2.
        if len(estados) == 1:
            estado1 = estados[0]; estado2 = "perdedor"
            puntaje1 = puntajes[0]
        else:
            estado1 = estados[0]; estado2 = estados[1]
            puntaje1 = puntajes[0]; puntaje2 = puntajes[1]
               
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
                    print("¡Empate triple!\n")
                    condicion = "Empate"
                else: 
                    print("¡Empate entre ambos jugadores!.\n")
                    condicion = "Empate"
            elif puntaje1 == puntajeD: 
                print(f"¡Empate entre {usuario} y el dealer!.\n")
                condicion = "Empate"
            else: 
                print(f"¡El ganador es {usuario} con {puntaje1} puntos!\n")
                condicion = "Victoria"
        elif puntaje2 == punt_max and estado2 != "perdedor":
            if puntaje2 == puntajeD: print("¡Empate entre el Jugador2 y el dealer!.\n")
            else: print(f"¡El ganador es Jugador2 con {puntaje2} puntos!\n")
        else: print(f"¡El ganador es el dealer con {puntajeD} puntos!\n")

        # Se guardan los resultados de la partida en el registro del jugador.
        est.crear_estadisticas(usuario, condicion)
