# Notas sobre el diseño de la aplicación.

## Tabla de contenidos.
1. [Descripción del problema](#descripción-de-problema)
2. [Planteamiento de la solución](#planteamiento-de-la-solución)
3. 
4.


## Descripción de problema.
Se desea diseñar una aplicación que juegue una partida de Blackjack para uno o dos jugadores y el dealer. 

Las reglas del Blackjack son las siguientes:

- Las cartas tienen un puntaje que va acorde con el valor de la carta. Las cartas "J", "Q" y "K" valen 10 puntos, el "A" puede valer 1 o 11 puntos.
- Al inicio del juego, se le dan dos cartas a cada jugador.
- Cuando es el turno de cada jugador, el jugador puede pedir todas las cartas que quiera de una en una:
    - Si el puntaje es mayor a 21, pierde.
    - Si obtuvo un puntaje especial, gana automáticamente.
    - Si su puntaje es menor o igual a 21, sigue en el juego.
- El dealer tiene una condición adicional: mientras su puntaje sea menor o igual a 16 está obligado a pedir una carta.
- Los puntajes especiales más típicos son estos:
    - Blackjack: 21 puntos con tan solo dos cartas.
    - Cinco menores: tener cinco cartas con valores menores a 10 y un puntaje total menor a 21.
    - Tres 7's: tener en la mano solamente tres "7" de cualquier palo.
- Si al finalizar todos los turnos ningún jugador gana por puntajes especiales, el ganador es quien tenga el puntaje más cercano pero menor a 21 (puntaje <= 21).

Además de las reglas del juego es necesario tomar en cuenta las siguientes consideraciones:

- La toma de datos debe ser por medio de la terminal.
- El usuario del programa debe ser capaz de registrar múltiples usuarios de juego.
- Para cada usuario creado debe ser posible obtener las estadísticas (fecha y resultado) de al menos las últimas 5 partidas jugadas.
- Al inicio del juego deben mostrarse las cartas de todos los jugadores y determinar si alguien obtuvo un Blackjack. El dealer siempre tiene una carta oculta.
- Durante cada turno debía presentarse la mano del jugador y actualizarla cada vez que tomara una carta. El dealer siempre tiene una carta oculta.
- El juego debe ser programado usando el paradigma de Programación Orientada a Objetos y además debe tener un diseño modular.

## Planteamiento de la solución.

Este diseño considera el uso de cuatro clases: Carta( ), Baraja( ), Mano( ) y Juego( ). A continuación se describen las funciones de cada uno de ellos:

- Carta( ): 
    - Las cartas de un naipe están conformadas por dos elementos: un valor y un palo. Así, la carta "2♥" tiene un valor de "2" y su palo es "♥".
    - El objeto carta debe ser capaz de crear las 52 cartas de una baraja y de retornar de manera separada su valor para así poder usarse a la hora de calcular los puntajes.
    - Además, se desea que Carta( ) muestre el valor y el palo juntos en un solo string, por motivos de facilidad a la hora de presentar los datos de la partida.

- Baraja( ):
    - El objeto baraja brinda una colección con los 52 objetos carta del naipe.
    - Baraja( ) debe ser capaz de mezclar las cartas de forma aleatoria.
    - Baraja ( ) debe ser capaz de repartir cartas a los jugadores.

- Mano( ):
    - El objeto tipo mano almacena las cartas que ha recibido cada jugador. De este modo, cuando el objeto baraja reparte una carta, el objeto mano es quien la recibe.
    - Mano( ) debe ser capaz de revelar sus cartas, así es posible saber cuál es la mano de cada jugador. Debe incluirse un modo adicional para el dealer, que durante la partida oculta una de sus cartas.

- Juego( ):
    - El objeto juego se apoya en los objetos de las otras clases para manejar la gran mayoría de las operaciones que se realizan durante la partida: 
        - Registra los usuarios que juegan la partida.
        - Crea una mano para cada usuario.
        - Inicializa una mazo y lo baraja.
        - Reparte dos cartas a cada jugador al inicio de la partida.
        - Se encarga de llevar a cabo los turnos de cada jugador y del dealer.
        - Se encarga de determinar al ganador de la partida.
    - Juego ( ) debe ser capaz de mostrar las cartas de todos los jugadores y el dealer en la ronda inicial, evaluar sus condiciones de victoria y determinar si alguien ganó.
    - De no tenerse un ganador, Juego( ) maneja los turnos de cada jugador y el dealer, evaluando sus puntajes y condiciones de victoria y determinando sus estados dentro del juego.

Adicional a las clases del programa, es necesario crear distintos módulos con funciones para poder manejar el resto de tareas:
- Módulo de estadísticas: contiene las funciones que se encargan de cargar, actualizar y mostrar las estadísticas al usuario.
    - Crear estadística nueva.
    - Cargar las estadísticas y mostrarlas.
- Módulo de manejo de usuarios: contiene las funciones que se encargan de crear, cargar y seleccionar el usuario que el jugador quiera utilizar.
    - Crear un nuevo usuario.
    - Mostrar lista de usuarios y escoger uno para jugar la partida.
- Módulo de comunicación con el jugador: contiene las funciones que muestran los dos principales menús que se ofrecen al jugador.
    - Menú inicial: opciones relacionadas con los usuarios - crear/usar usuario existente, salir.
    - Menú de usuario: opciones específicas para el usuario elegido - jugar, estadísticas, salir.

## Pseudocódigos.
Este pseudocódigo explica el funcionamiento general del programa.