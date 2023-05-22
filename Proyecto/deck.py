import random

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

    def mostrar_cartas(self, usuario, modo="jugador"):
        if modo == "jugador":
            print(f"Mano de {usuario}:")
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

# --------METODOS PARA OBTENER INFO DEL NAIPE------.
# print(baraja.baraja[i])  # Obtener una carta de la baraja.
# print(baraja.baraja[i].palo)  # Obtener el palo de esa carta.
# print(baraja.baraja[i].valor)  # Obtener el valor de esa carta.
# print(puntos.get(baraja.baraja[i].valor))  # Obtener los puntos que vale esa carta.