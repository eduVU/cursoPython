import clases

# BORRADOR PARA LA CLASE "JUEGO".

# jugadores = int(input("Ingrese el número de jugadores: "))

# for i in range(jugadores):



lista_jugadores = ['dealer', 'jugador1', 'jugador2']

# Se genera un nuevo mazo y se baraja.
mazo = clases.Baraja()
mazo.barajar()

# Se inicia la partida con un jugador y el dealer.
jugador = clases.Mano()
dealer = clases.Mano()


print(mazo.baraja)
print(len(mazo.baraja))

mazo.repartir(jugador,inicial=True)
jugador.mostrar_cartas()

mazo.repartir(dealer,inicial=True)
dealer.mostrar_cartas(modo="dealer")

print(mazo.baraja)
print(len(mazo.baraja))

mazo.repartir(jugador)
jugador.mostrar_cartas()

mazo.repartir(dealer)
dealer.mostrar_cartas(modo="dealer")

print(mazo.baraja)
print(len(mazo.baraja))