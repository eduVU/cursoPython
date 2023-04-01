# Tarea 1

## Elaborado por: Eduardo Villalobos Ugalde.

### Problema 1: Comprobar si una palabra es un palíndromo.

#### Paso 1: Entender el problema.

Una palabra es un palíndromo si esta dice lo mismo cuando se lee de derecha a izquierda en comparación con leerla de izquierda a derecha. Es decir, si invertimos completamente el orden de las letras de la palabra, el resultado dice lo mismo que la palabra original.  
Para detectar si una palabra es un palíndromo se podrían tomar dos muestras: una que tenga la palabra original y otra con la palabra invertida, y compararlas entre sí. 

Para efectos de una frase, sería mejor capturar el contenido de la frase eliminando los espacios en blanco que separan a cada palabra que contiene y considerarla como *una única palabra compuesta solamente por letras*, de modo que pueda usarse el mismo método ya descrito para detectar palíndromos en palabras.

#### Paso 2: Planear.

1. ¿Se necesita una interfaz de usuario? Sí, el programa debe ser capaz de recibir una palabra o frase que ingrese el usuario. La interfaz solo debe especificar que se va a recibir una palabra/frase a continuación, de modo que no es necesaria una interfaz gráfica compleja.
2. ¿Cuáles son los inputs del programa y su proveniencia? El único input es la palabra/frase que se necesita para la comprobación, esta es proporcionada por el usuario por medio de la terminal usando el teclado.
3. ¿Cuáles son los outputs del programa? El programa consiste en una respuesta acerca de si una palabra/frase es un palíndromo, por lo tanto hay un único output de naturaleza *verdadero/falso*. Puede usarse una respuesta más detallada, pero el objetivo es afirmar o negar si la palabra/frase es un palíndromo.
4. ¿Dado el input, cuáles son los pasos necesarios para llegar al output? A continuación se presenta un pseudocódigo que pretende detallar este proceso:

    > Pedir una palabra o frase al usuario: `Ingrese una palabra o frase`. Se recibe el **input**.

    > Eliminar los espacios en blanco que contiene el input y guardar el resultado como una sola palabra que solo tenga letras: creación del **Elemento A**.

    > Invertir el orden de las letras del Elemento A y guardar el resultado: creación del **Elemento B**.

    > Comparar el Elemento A con el Elemento B y entregar el **output**:
    > - Si los elementos son iguales, imprimir `La palabra/frase es un palíndromo`.
    > - Si los elementos son distintos, imprimir `La palabra/frase no es un palíndromo`. 

#### Paso 3: Dividir y conquistar.

Se propone separar este problema en 3 subproblemas:

1. Recibir una palabra/frase, eliminar los espacios en blanco que contenga y obtener una sola palabra compuesta por letras, obtener el Elemento A.
2. Tomar el resultado del paso anterior e invertir el orden de sus letras, obtener el elemento B.
3. Realizar la comparación de los elementos A y B y entregar un resultado al usuario.

### Problema 2: Crear un programa que borre los logs a diario, excepto los que contienen la palabra "error". Estos se copian al directorio "Errores" y se envía un correo al administrador.

#### Paso 1: Entender el problema.

El programa es ejecutado cada 24 horas, toma todos los logs existentes hasta ese momento y los revisa palabra por palabra, si un log contiene la palabra "error", se hace una copia de ese log en el directorio "Errores", se envía un mensaje personalizado a la dirección de correo electrónico del administrador y se borra el log original para que no vuelva a inspeccionarse en el futuro. Si un log no contiene la palabra clave, este se borra y no se toman acciones adicionales.

#### Paso 2: Planear.

1. ¿Se necesita una interfaz de usuario? No, el programa no necesita interactuar directamente con un usario para realizar sus tareas, funciona con base en los contenidos del directorio que monitorea y los atributos ya definidos: dirección de correo electrónico, ubicación del directorio "Errores", etc.
2. ¿Cuáles son los inputs del programa y su proveniencia? Los inputs principales son cada uno de los logs que el programa monitorea, si existen N logs al terminar el periodo de 24 horas, entonces hay N inputs. También se consideran como inputs la dirección de correo electrónico del administrador y la ubicación del directorio "Errores", pues sin ellos no es posible entregar un resultado satisfactorio. Además, podría considerarse el contador de tiempo como un input pues el programa no inicia sus funciones hasta que pasen 24 horas desde su última ejecución.
3. ¿Cuáles son los outputs del programa? Considerando un output como una "acción" o "resultado", el output principal sería que se borren los logs. En caso de que se detecte la palabra "error", se añaden la copia del log en el directorio "Errores" y el correo electrónico de notificación como outputs.
4. ¿Dados los inputs, cuáles son los pasos necesarios para llegar a los outputs? A continuación se presenta un pseudocódigo que pretende detallar este proceso:

    > Condiciones o **inputs** iniciales, no es necesario setearlas cada vez que el programa corre: 
    > - Crear un contador de tiempo.
    > - Configurar y autenticar el acceso a un correo electrónico (por ejemplo, Gmail) para este programa.
   
    > Cuando el contador de tiempo llegue a 24 horas, el programa inicia la revisión de todos los logs que hay en el directorio hasta ese momento. Se reinicia el contador.

    > Abrir el primer log y buscar la palabra "error" en él, se definen los siguientes **outputs** según el resultado de la búsqueda:
    > - Si la palabra "error" existe en el log: se copia este log al directorio "Errores" especificado y el programa envía este mensaje a la dirección de correo del administrador: `Se ha registrado un nuevo mensaje de error`. El log original se borra.
    > - Si la palabra "error" no existe en el log: se elimina el log original.

    > Se repite el bloque anterior para cada uno de los logs disponibles. Una vez se revise el último log, el programa queda en espera de que el contador alcance 24 horas de nuevo.

#### Paso 3: Dividir y conquistar.

Se propone separar este problema en 5 subproblemas:

1. Crear un contador de tiempo y un método para reiniciarlo, así como conectar el programa a una cuenta de correo electrónico autorizada.
2. Abrir un log y buscar palabras clave dentro él, en este caso la palabra "error".
3. Crear un código que borre un log y otro que copie un log en el directorio "Errores".
4. Crear un código que envíe un correo electrónico personalizado al administrador, usando las credenciales definidas en el paso 1.
5. Crear una secuencia que repita los pasos 2, 3 y 4 para cada uno de los logs que hay en el directorio.

### Problema 3: Crear un programa que reciba un número entero y determine si, al reordenar los dígitos de cualquier manera, se obtenga un número que sea múltiplo de 5.

#### Paso 1: Entender el problema.

Si un número entero es múltiplo de 5, quiere decir que ese número es divisible por 5. Cualquier número entero es divisible por 5 únicamente si el dígito que ocupa el valor de las unidades es un **0 o 5**. Entonces, se necesita crear un programa que revise cada uno de los dígitos de un número entero dado: basta con que al menos uno de ellos sea 0 o 5 para que se pueda construir un número entero múltiplo de 5, pero el resultado es negativo si y solo si se revisaron todos los dígitos y ***ninguno*** es un 0 o 5.

#### Paso 2: Planear.

1. ¿Se necesita una interfaz de usuario? Sí, el programa debe ser capaz de recibir un número entero que ingrese el usuario. La interfaz solo debe especificar que se va a recibir un número entero de modo que no es necesaria una interfaz gráfica compleja. 
2. ¿Cuáles son los inputs del programa y su proveniencia? El único input es el número entero que se necesita para la comprobación, este es proporcionado por el usuario por medio de la terminal usando el teclado.
3. ¿Cuáles son los outputs del programa? El programa consiste en una respuesta acerca de si un número entero puede reordenarse para obtener un múltiplo de 5, por lo tanto hay un único output de naturaleza *verdadero/falso*. Puede usarse una respuesta más detallada, pero el objetivo es afirmar o negar si se puede obtener un múltiplo de 5 al reordenar los dígitos del número ingresado.
4. ¿Dado el input, cuáles son los pasos necesarios para llegar al output? A continuación se presenta un pseudocódigo que pretende detallar este proceso:

    > Pedir un número entero al usuario: `Ingrese un número entero`. Se recibe el **input** y se verifica que sea un número entero:
    > - Si el número no es un número entero, se genera un mensaje de error: `El valor ingresado no es un número entero` y se solicita de nuevo un número entero.
    > - Si el número es un número entero: se continúa al siguiente paso.

    > Se toma el número entero y se separa por dígitos.

    > Se analiza cada uno de los dígitos y se entrega el **output**:
    > - Si alguno de los dígitos es un 0 o un 5: imprimir `Es posible obtener un múltiplo de 5 al reordenar los dígitos de este número`.
    > - Si ninguno de los dígitos es un 0 o un 5: imprimir `No es posible obtener un múltiplo de 5 al reordenar los dígitos de este número`

#### Paso 3: Dividir y conquistar.

Se propone separar este problema en 3 subproblemas:

1. Recibir un número y comprobar que sea un número entero.
2. Tomar el número del paso anterior y separarlo en dígitos.
3. Para cada uno de los dígitos, comprobar si su valor es igual a 0 o 5. Entregar un resultado al usuario.