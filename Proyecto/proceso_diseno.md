# Notas sobre el diseño de la aplicación.

## Tabla de contenidos.
1. [Descripción del problema](#descripción-de-problema)
2. [Planteamiento de la solución](#planteamiento-de-la-solución)
3. [Pseudocódigos](#pseudocódigos)
4. [Dividir y conquistar: planteamiento de subproblemas](#dividir-y-conquistar-planteamiento-de-subproblemas)
5. [Implementación de código para resolver los subproblemas](#implementación-de-código-para-resolver-los-subproblemas)

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

### Este pseudocódigo explica el funcionamiento general del programa: 

![Pseudocódigo general](/Proyecto/pseudo_1.png "Pseudocódigo general")

### El bloque nombrado "Jugar el turno de los jugadores" se detalla a continuación:

![Pseudocódigo turno_J](/Proyecto/pseudo_2.png "Pseudocódigo turno jugador")

### El bloque nombrado "Jugar el turno del dealer" se detalla a continuación:

![Pseudocódigo turno_D](/Proyecto/pseudo_3.png "Pseudocódigo turno dealer")

## Dividir y conquistar: planteamiento de subproblemas.
Se propone separar el problema en los siguientes subproblemas:

1. Creación del módulo de estadísticas y sus dos funciones principales.
2. Creación del módulo de manejo de usuarios y sus dos funciones principales.
3. Desarrollo de la primera mitad del módulo principal y creación del módulo de comunicación con el jugador.
4. Creación de las clases Carta( ), Baraja( ) y Mano( ) con los atributos y métodos necesarios para realizar las tareas ya planteadas.
5. Creación de la clase Juego( ) con los atributos y métodos necesarios para realizar las tareas ya planteadas.
6. Desarrollo de la segunda mitad del módulo principal e integración con Juego ( ).

## Implementación de código para resolver los subproblemas.
A continuación se describe el proceso para implementar el código que resuelve cada subproblema. Durante la explicación se brindan los nombres finales que tienen los archivos, clases y funciones utilizadas en el código. 

Por favor refiérase a los comentarios internos del código para más información sobre cómo trabaja cada bloque de código.

### 1. Creación del módulo de estadísticas.
- Se creó el archivo llamado `estadisticas.py`.
- Se creó la función para crear estadísticas, llamada `crear_estadisticas(usuario, condicion)`. La función recibe el nombre de usuario y la condición del usuario (victoria, empate o derrota).
    - Obtener la fecha (`import datetime`).
    - Abrir/crear un archivo `est_{usuario}.txt`.
    - Agregar una línea con el formato "Fecha_hora: condición", cerrar el archivo.
- Se creó la función para cargar las estadísticas, llamada `ver_estadisticas(usuario)`. La función solo necesita el nombre de usuario que se quiere consultar.
    - Abrir el archivo `est_{usuario}.txt`.
    - Se crea una lista vacía llamada `estadisticas`. La lista se llena con cada línea leída del archivo. Se cierra el archivo.
    - Si la lista sigue vacía, se informa al usuario que no hay nada que mostrar.
    - Si la lista no está vacía, se imprimen las últimas 5 líneas del archivo (los últimos 5 índices de la lista).

### 2. Creación del módulo de manejo de usuarios y sus dos funciones principales.
- Se creó el archivo llamado `manejo_usuarios.py`.
- Se creó la función para cargar usuarios, llamada `cargar_usuarios()`.
    - Abrir/crear un archivo llamado `usuarios.txt`.
    - Se crea una lista vacía llamada `usuarios`. La lista se llena con cada línea leída del archivo pero se elimina el salto de línea "\n". Se cierra el archivo.
    - La función retorna la lista.
- Se creó la función para elegir un usuario, llamada `escoger_usuario()`.
    - Primero, se cargan los usuarios con  `usuario = cargar_usuarios()`.
    - Si la lista `usuario` está vacía, se notifica al jugador que no hay usuarios para escoger.
    - Si la lista no está vacía, se imprimen los valores de la lista y se pide al usuario escoger uno.
    - Si el usuario ingresa un nombre que no coincide con los mostrados, se muestra el error correspondiente.
    - Si el usuario sí existe, se retorna el usuario elegido.
- Se creó la función para crear un usuario, llamada `crear_usuario()`.
    - Primero, se cargan los usuarios con  `usuario = cargar_usuarios()`.
    - Se pide el nombre del nuevo usuario. Si este ya se encuentra en la lista `usuario`, se notifica el error al usuario.
    - Si el usuario no existe en la lista, se abre el archivo `usuarios.txt`, se agrega una línea con el nombre y se cierra el archivo.
    - Se retorna el nuevo usuario.
    
### 3. Desarrollo de la primera mitad del módulo principal y creación del módulo de comunicación con el jugador.
- Se creó el módulo principal, llamado `main.py`.
- El programa corre sobre un bucle infinito, así es posible jugar varias partidas consecutivas. La variable de control para salir del bucle se llama `interruptor` y su valor inicial es `interruptor = "ok"`.
- Se creó el archivo llamado `comunicacion.py` para crear las funciones con los menús:
    - La primera función, llamada `menu_usuarios()`, presenta al usuario tres opciones: usuario nuevo, crear usuario y salir.
        - Si se elige salir, retorna `interruptor = "salir"` y el programa principal termina.
        - En cualquier otro caso, llama a las funciones `crear_usuario()` o `escoger_usuario()` según corresponda.
    - La primera función, llamada `menu_usuarios2(usuario)`, recibe el usuario en uso y presenta al usuario tres opciones: nueva partida, ver estadísticas y salir.
        - Salir funciona igual que en la función anterior.
        - Ver estadísticas llama a la función `ver_estadisticas(usuario)`.
        - Nueva partida inicia el juego.
- El módulo principal recibe el usuario elegido retornado por la función `menu_usuarios()` y posibles señales de interrupción de ambas funciones del menú. Si no hay interrupciones se inicia el juego en la segunda parte del módulo.

### 4. Creación de las clases Carta( ), Baraja( ) y Mano( ) con los atributos y métodos necesarios para realizar las tareas ya planteadas.
- Estas clases se agruparon en un módulo llamado `deck.py` pues son afines.
- La clase `Carta()` utiliza una lista con los nombres de las cartas y otra con los palos del naipe para crear un objeto tipo carta: `self.palo` y `self.valor`.
- La clase `Baraja()` crea una lista con 52 objetos del tipo carta para crear `self.baraja`.
    - Además, el método `self.barajar()` permite mezclar a `self.baraja` aleatoriamente.
    - Finalmente, el método `self.repartir(other, inicial=False` otorga cartas a los demás jugadores.
        - Utiliza `other` porque recibe atributos del objeto `Mano()` para saber a quién dar las cartas antes de eliminarlas de `self.baraja`.
        - `inicial=True` indica que se den dos cartas al jugador, `inicial=False` reparte solo una carta.
- La clase `Mano()` contiene una lista con las cartas del objeto: `self.mano`.
    - El método `self.mostrar_cartas(usuario, modo="jugador")` muestra las cartas en la mano.
        - Depende de `usuario` para declarar de quién es la mano que se muestra.
        - `modo="jugador"` dicta si se enseñan todas las cartas o si se mantiene una en secreto con `modo="dealer"`.
