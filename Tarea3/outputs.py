# Este módulo maneja los distintos mensajes de error, el mensaje de ayuda y la escritura de resultados en un archivo específico.

from datetime import datetime  # Módulo para obtener la fecha y hora.

# Esta función se llama para mostrar la guía del programa.
def mostrar_ayuda():
    ayuda = """\nEsta calculadora utiliza números enteros para calcular sumas, restas, multiplicaciones, divisiones, factoriales y potencias.
Primero, seleccione la operación que desea realizar o ingrese "salir" para cerrar el programa. Las palabras pueden ser escritas con mayúsculas 
o minúsculas y el programa las puede reconocer. A continuación se describe cada una de las operaciones:

Suma: calcula la suma de n números. Los números se ingresan en una sola línea separados por espacios, ej: si ingreso "1 5 23" el resultado será 29.

Resta: calcula la resta de dos números. Los números se ingresan en una sola línea separados por espacio y la resta se calcula con el formato "num1 - num2", ej: si se ingresa "20 5" el resultado será 15.

Multiplicación: calcula un producto entre n números. Los números se ingresan en una sola línea separados por espacio, ej: si ingreso "1 5 2" el resultado será 10.

División: calcula la división entre dos números. Los números se ingresan en una sola línea separados por espacio y la división se calcula con el formato "num1/num2", ej: si se ingresa "20 5" el resultado será 4.
La división no permite que el divisor sea cero pues genera una forma indeterminada.

Factorial: calcula el factorial de un número entero dado. El factorial no existe para números negativos y el factorial de cero es uno (0! = 1).

Potencia: calcula la potencia que se obtiene al usar los dos números dados en una sola línea y separados por espacio, usando el formato "num1**num2". Por ejemplo, si se ingresa "2 3" la potencia será 2**3 = 8.
La potencia 0**0 no es permitida pues genera una forma indeterminada.

El menú de ayuda o la opción de salir siempre están disponibles desde el menú principal.
Por favor revise que no ingrese espacios en blanco adicionales a la hora de seleccionar una opción o ingresar números.\n
"""
    print(ayuda)

# Esta función muestra un mensaje de error cada vez que se ingresa una opción inválida en el menú de operaciones.
def notificar_error_menu():
    print('ERROR:se ha seleccionado una opción que no existe en el menú de operaciones.\n')

# Esta función muestra un mensaje de error cada vez que se ingresa un dato inválido a la hora de hacer una operación.
def notificar_error_operaciones():
    print("ERROR: se han ingresado datos inválidos para la operación seleccionada, ingrese a la ayuda para obtener más información.")

# Esta función se encarga de escribir el tipo de operación, el resultado y la fecha y hora en la que se realizó la operación en un archivo .log.
def escribir_archivo(operacion, total):
    fecha_hora = datetime.now()  # Variable que contiene la fecha y hora
    fecha_hora = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")  # Se da formato a la fecha y hora.
    file = open("resultados.log", "a")
    file.write("{} Operacion: {}, resultado: {}\n".format(fecha_hora, operacion, total))
    file.close()