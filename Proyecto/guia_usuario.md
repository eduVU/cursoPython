# Guía de usuario

## Tabla de contenidos.

1. [Descripción de las opciones de usuario](#descripción-de-las-opciones-de-usuario)
    - [Menú general](#1-menú-general)
    - [Menú de usuario](#2-menú-de-usuario)
    - [Menú de modo de juego](#3-menú-de-modo-de-juego)
    - [Menú de turno](#4-menú-de-turno)
2. [Dinámica y reglas del juego](#dinámica-y-reglas-del-juego)
3. [Condiciones de victoria](#condiciones-de-victoria)

## Descripción de las opciones de usuario.

A continuación se detallan los menús que ofrece el programa en sus distintas etapas:

### 1. Menú general. 
Este es el primer menú que despliega el programa cuando se inicia.

a. Crear un usuario nuevo: 
- Al seleccionar esta opción el usuario puede ingresar cualquier nombre de usuario que desee, utilizando mayúsculas, minúsculas, números y caracteres especiales. 
- El programa le notificará si el usuario elegido ya existe, de ser así el usuario será redirigido al inicio del menú.
- En caso de que el usuario no existiera previamente, se registrará este nuevo usuario en el archivo llamado "usuarios.txt".
   
b. Usar un usuario existente:
- Se muestran al usuario todos los nombres de usuario presentes en el archivo "usuarios.txt". El usuario debe ingresar el nombre de usuario que desea utilizar.
- El programa le notificará al usuario si ha elegido un nombre que no está en la lista y este será redirigido al inicio de 

c. Salir: cierra el programa.

### 2. Menú de usuario. 
Se accede a este menú luego de elegir o crear un usario.

a. Nueva partida: 
- Se inicia una nueva partida de Blackjack con el usuario escogido. Ver [Dinámica y reglas del juego](#dinámica-y-reglas-del-juego) para obtener más detalles.
   
b. Estadísticas:

- Se muestran las estadísticas del usuario seleccionado, muestra como máximo los resultados de las últimas 5 partidas.
- Las estadísticas poseen este formato: "Fecha: Resultado", donde el resultado puede ser "Victoria", "Empate" o "Derrota".
- Las estadísticas de cada usuario se guardan en un archivo específico cuyo nombre tiene este formato: "est_{usuario}.txt".
- El programa le notificará al usuario si el nombre de usuario que se consulta no tiene ninguna partida registrada y lo devolverá al inicio del menú.

c. Salir: cierra el programa.

### 3. Menú de modo de juego. 
Se accede a este menú al iniciar una nueva partida.

a. Solo: 
- El juego inicia con dos participantes en total: el usuario y el dealer.

b. Duo: 
- El juego inicia con tres participantes en total: el usuario, un segundo jugador llamado "Jugador2" y el dealer.
- "Jugador2" es un jugador invitado, por lo tanto no genera estadísticas propias aunque sí puede ganar, perde o empatar la partida.


### 4. Menú de turno. 
Se accede este menú durante la partida cada vez que el jugador deba tomar una acción.

a. Pedir una carta:
- Se agrega una carta a la mano del jugador. Ver [Dinámica y reglas del juego](#dinámica-y-reglas-del-juego) para obtener más detalles.
   
b. Terminar el turno:
- El jugador termina su turno y se continúa con los demás participantes.

## Dinámica y reglas del juego.

Este juego recrea una partida de Blackjack que incluye un máximo de dos jugadores y el dealer. 
- En Blackjack, cada carta tiene un puntaje según el valor de la carta: un "2" vale 2 puntos, el "7" vale 7 puntos, etc.
- Las cartas "J", "Q" y "K" tienen un valor de 10 puntos.
- La carta "A" puede valer tanto 1 como 11 puntos, según convenga.
- El jugador pierde si los puntos totales de su mano sobrepasan 21 puntos.

Al inicio de cada partida, se reparte una mano de dos cartas a cada jugador y al dealer. La mano de los jugadores es visible y la del dealer solo muestra una carta.

Una vez repartida la mano, se evalúa si alguien obtuvo una victoria al conseguir un Blackjack, de ser así el juego termina (ver [Condiciones de victoria](#condiciones-de-victoria)) para más detalles.

Luego se juegan los turnos de cada jugador en este orden: turno del usuario, turno del Jugador2 (sí está presente) y turno del dealer.
- Durante su turno, el jugador puede pedir cartas o pasar su turno (ver [Menú de turno](#4-menú-de-turno)).
- El jugador puede pedir tantas cartas como desee, pero si su puntaje sobrepasa 21 puntos pierde automáticamente.
- Una vez que un jugador pasa su turno, no puede volver a pedir más cartas y su puntaje es final.

Cuando los jugadores terminan sus turnos, el dealer realiza sus acciones:
- El dealer debe pedir una carta siempre y cuando su puntaje sea menor o igual a 16.
- De igual manera, si el puntaje del dealer excede 21 puntos, este pierde automáticamente.

## Condiciones de victoria
Existen distintas puntuaciones especiales que garantizan una victoria automática a quien la obtenga:
- Blackjack: consiste en conseguir 21 con tan solo dos cartas, es decir, tener un "A" y ya sea un "10", "J", "Q" o "K". Dado que puede haber más de un Blackjack en la ronda inicial, se permiten empates bajo dicha condición.
- Cinco menores: consiste en tener en la mano cinco cartas con valor menor a 10 y su puntaje sea menor o igual a 21 (ej: "A", "5", "5", "2" y "3").
- Tres 7's: como el nombre sugiere, consiste en tener una mano conformada únicamente por tres "7".

En caso de que ningún jugador consiguiera una puntuación especial, el ganador será aquel que consiga el puntaje más cercano a 21 sin sobrepasarse.