import random

# Diccionario con puntaje para cada carta dentro del juego según su valor.
puntos = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Componentes de cada carta: un palo y un valor.
palos = ('\u2764', '\u2666', '\u2660', '\u2618')
valores = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

# Esta clase construye las cartas a partir de un valor (ej: K) y un palo (ej: ♥).
class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    # Se define cómo se presentan los strings dentro de esta clase.
    def __str__(self):
        return "".join([self.valor, self.palo])

class Baraja:
    def __init__(self):
        self.baraja = []
        # Se crea una baraja con 52 cartas.
        for valor in valores:
            for palo in palos:
                carta = Carta(palo, valor)
                self.baraja.append(carta)

    # Esta función mezcla las cartas de la baraja de forma aleatoria.
    def barajar(self):
        random.shuffle(self.baraja)

    # Función para repartir cartas al inicio del juego y durante cada turno posterior.
    def repartir(self,other,inicial=False):
        if inicial == True:  # Al inicio del juego se dan dos cartas a cada jugador.
            for i in range(2):
                other.mano.append(self.baraja[0])
                self.baraja.pop(0)
        elif inicial == False:
            other.mano.append(self.baraja[0])
            self.baraja.pop(0)

class Mano():
    def __init__(self):
        self.mano = []

    def mostrar_cartas(self, modo="jugador"):
        if modo == "jugador":
            print("Mano del jugador:")
            print(*self.mano)
            print("\n")
        if modo == "dealer":
            mano = []
            for i in range(len(self.mano)):
                if i == 0:
                    mano.append("?")
                else:
                    mano.append(self.mano[i])
            print("Mano del dealer:")        
            print(*mano)
            print("\n")        

class Juego():
    def __init__(self, usuarios):
        self.puntos = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                       '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    # NO FUNCIONA
    # Esta función cuenta los puntos en la mano del jugador y define si ganó, perdió o sigue jugando.   
    def calcular_puntaje(jugador):
        puntaje = 0
        # Se calcula el puntaje según la mano del jugador.
        for i in range(len(jugador.mano)):
            puntaje = puntaje + puntos.get(jugador.mano[i].valor)
        return puntaje

    # NO FUNCIONA
    # Se evalúan las condiciones de la partida para elegir un ganador.
    def definir_ganador(estado1,estado2,puntaje1=0,puntaje2=0, puntajeD=0):
        if puntaje1 == max(puntaje1, puntaje2, puntajeD) and estado1 != "perdedor": 
            if puntaje1 == puntaje2:
                print("¡Empate! Ganan ambos jugadores.")
            elif puntaje1 == puntajeD:
                print("¡Empate! Ganan el Jugador1 y el dealer.")
            else:
                print("¡El ganador es Jugador1!")
        elif puntaje2 == max(puntaje1, puntaje2, puntajeD) and estado2 != "perdedor":
            if puntaje2 == puntajeD:
                print("¡Empate! Ganan el Jugador2 y el dealer.")
            else:
                print("¡El ganador es Jugador2!")
        else: 
            print("¡El ganador es el dealer!")
        exit()


# Metodos para obtener info del naipe.
# print(baraja.baraja[i])  # Obtener una carta de la baraja.
# print(baraja.baraja[i].palo)  # Obtener el palo de esa carta.
# print(baraja.baraja[i].valor)  # Obtener el valor de esa carta.
# print(puntos.get(baraja.baraja[i].valor))  # Obtener los puntos que vale esa carta.