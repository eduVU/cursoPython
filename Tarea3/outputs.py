# Este módulo maneja los distintos mensajes de error, el mensaje de ayuda y la escritura de resultados en un archivo específico.


def mostrar_ayuda():
    ayuda = """\nEsta calculadora utiliza números enteros para calcular sumas, restas, multiplicaciones, divisiones, factoriales y potencias.
Primero, seleccione la operación que desea realizar o ingrese "salir" para cerrar el programa. Las palabras pueden ser escritas con
mayúsculas o minúsculas y el programa las puede reconocer. A continuación se describe cada una de las operaciones:

Suma: calcula la suma de n números. Los números se ingresan en una sola línea separados por espacios, ej: si ingreso "1 5 23" el resultado será 29.

Resta: calcula la resta de dos números. Los números se ingresan en una sola línea separados por espacio y la resta se calcula con el formato "num1 - num2", ej: si se ingresa "20 5" el resultado será 15.

Multiplicación: calcula un producto entre n números. Los números se ingresan en una sola línea separados por espacio, ej: si ingreso "1 5 2" el resultado será 10.

División: calcula la división entre dos números. Los números se ingresan en una sola línea separados por espacio y la división se calcula con el formato "num1/num2", ej: si se ingresa "20 5" el resultado será 4.

Factorial: calcula el factorial de un número entero dado. El factorial no existe para números negativos y el factorial de cero es uno (0! = 1).

Potencia: calcula la potencia que se obtiene al usar los dos números dados en una sola línea y separados por espacio, usando el formato "num1**num2". Por ejemplo, si se ingresa "2 3" la potencia será 2**3 = 8.
        
El menú de ayuda o la opción de salir siempre están disponibles desde el menú principal.\n
"""
    print(ayuda)

def notificar_error_menu():
    print('ERROR:se ha seleccionado una opción que no existe en el menú de operaciones.\n')

def notificar_error_operaciones():
    print("""ERROR: se han ingresado datos inválidos para la operación seleccionada, ingrese al menú de ayuda
para obtener más información.
    """)

def escribir_archivo(operacion, total):
    return
