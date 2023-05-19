import random
valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

palos = ('\u2764', '\u2666', '\u2660', '\u2618')
atributos = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

class Carta:
    def __init__(self, palo, atributo):
        self.palo = palo
        self.atributo = atributo

    def __str__(self):
        return " ".join([self.atributo, self.palo])

class Baraja:
    def __init__(self):
        # Se definen los cuatro palos de la baraja.
        self.palo_trebol = ["A♣","2♣","3♣","4♣","5♣","6♣","7♣",
                       "8♣","9♣","10♣","J♣","Q♣","K♣"]

        self.palo_corazon = ["A♥","2♥","3♥","4♥","5♥","6♥","7♥",
                        "8♥","9♥","10♥","J♥","Q♥","K♥"]

        self.palo_pica = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠",
                     "8♠","9♠","10♠","J♠","Q♠","K♠"]

        self.palo_diamante = ["A♦","2♦","3♦","4♦","5♦","6♦","7♦",
                         "8♦","9♦","10♦","J♦","Q♦","K♦"]
        # La baraja surge que la combinación de todos los palos.
        self.baraja = self.palo_trebol + self.palo_pica + self.palo_corazon + self.palo_diamante

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
            print(f"{self.mano}")
        if modo == "dealer":
            mano = []
            for i in range(len(self.mano)):
                if i == 0:
                    mano.append("?")
                else:
                    mano.append(self.mano[i])
            print(f"{mano}")


