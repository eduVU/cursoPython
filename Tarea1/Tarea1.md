# Tarea 1

## Elaborado por: Eduardo Villalobos Ugalde.

### Problema 1: Comprobar si una palabra es un palíndromo.

#### Paso 1: Entender el problema.

Una palabra es un palíndromo si esta dice lo mismo cuando se lee de derecha a izquierda en comparación con leerla de izquierda a derecha. Es decir, si invertimos completamente el orden de las letras de la palabra, el resultado dice lo mismo que la palabra original.  
Para detectar si una palabra es un palíndromo tendría que tomarse dos muestras: una que tenga la palabra original y otra con la palabra invertida, y compararlas entre sí. 

Para efectos de una frase, sería mejor capturar el contenido de la frase eliminando los espacios en blanco que separan a cada palabra que contiene y considerarla como *una única palabra compuesta solamente por letras*, de modo que pueda usarse el mismo método ya descrito para detectar palíndromos en palabras.

#### Paso 2: Planear.

1. ¿Se necesita una interfaz de usuario? Sí, el programa debe ser capaz de recibir una palabra o frase que ingrese el usuario. La interfaz solo debe especificar que se va a recibir una palabra/frase a continuación, de modo que no es necesaria una interfaz gráfica compleja. 
2. ¿Cuáles son los Inputs del programa y su proveniencia? El único input es la palabra/frase que se necesita para la comprobación, esta es proporcionada por el usuario por medio de la terminal usando el teclado.
3. ¿Cuál es el Output del programa? El programa consiste en una validación de sí una palabra/frase es un palíndromo, por lo tanto el output debe ser de naturaleza *verdadero/falso*. Puede usarse una respuesta más detallada, pero el objetivo es afirmar o negar si la palabra/frase es un palíndromo.
4. ¿Dado el input, cuáles son los pasos necesarios para llegar al output? A continuación se presenta un pseudocódigo que pretende detallar este proceso:

    > Pedir una palabra o frase al usuario: se recibe el **input**.

    > Eliminar los espacios en blanco que contiene el input y guardar el resultado como una sola palabra que solo tenga letras: creación del **Elemento A**.

    > Invertir el orden de las letras del Elemento A y guardar el resultado: creación del **Elemento B**.

    > Comparar el Elemento A con el Elemento B y entregar el **output**:
        - Si los elementos son iguales, imprimir `La palabra/frase es un palíndromo`.
        - Si los elementos son distintos, imprimir `La palabra/frase no es un palíndromo`. 

#### Paso 3: Dividir y conquistar.

Se propone separar este problema en 3 subproblemas:

1. Recibir una palabra/frase, eliminar los espacios en blanco que contenga y obtener una sola palabra compuesta por letras, obtener el Elemento A.
2. Tomar el resultado del paso anterior e invertir el orden de sus letras, obtener el elemento B.
3. Realizar la comparación de los elementos A y B y entregar un resultado al usuario.