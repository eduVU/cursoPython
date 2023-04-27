# Programa para intercalar palabras y convertirlas a mayuscula/minuscula según se pida usando un módulo.

import manipulacion

while True:
    palabra1 = input('Ingrese la primera palabra: ')
    if palabra1 == 'salir':
        break

    palabra2 = input('Ingrese la segunda palabra: ')
    if palabra2 == 'reiniciar':
        continue

    modo = input('Seleccione qué desea hacer con las palabras (intercalar/mayus/minus): ')
    if modo == 'intercalar':
        salida = manipulacion.intercalar(palabra1, palabra2)
        print(salida)

    elif modo == 'mayus':
        salida1, salida2 = manipulacion.mayuscula(palabra1,palabra2)
        print(salida1, salida2)
    
    elif modo == 'minus':
        salida1, salida2 = manipulacion.minuscula(palabra1,palabra2)
        print(salida1, salida2)