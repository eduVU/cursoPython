""" Módulo principal del programa. Este módulo interactúa con el usuario por medio de la terminal, recibe los datos del usuario, llama
a todas las funciones de los otros módulos para realizar las operaciones necesarias, entregar los resultados finales y mostrar los
mensajes de error cuando es necesario.
"""

import aritmetica
import outputs

# Mensaje de bienvenida con instrucciones, se muestra solo una vez.
print('Gracias por usar esta calculadora de números enteros. En el menú principal puede ingresar la palabra "Ayuda" para mostrar la info de ayuda o la palabra "Salir" para salir del programa.\n')

# Esta tupla contiene las opciones válidas para ingresar en el menú principal.
opciones = ("suma", "resta", "mult", "div", "factorial", "potencia", "ayuda", "salir")

# Ciclo principal del programa.
while True:
    modo = input('Ingrese la operación que desea realizar (suma/resta/mult/div/factorial/potencia): ')
    
    # Se verifica que la opción escogida sea válida y se opera según corresponda para cada opción.
    if modo.lower() not in opciones:
        outputs.notificar_error_menu()
        continue
    elif modo.lower() == 'ayuda':
        outputs.mostrar_ayuda()
        continue
    elif modo.lower() == 'salir':
        break
    else:
        # se hacen las operaciones matemáticas, se utiliza try/except para filtrar entradas que no sean números enteros o valores indeseados.
        try:
            if modo.lower() == 'suma':
                elementos = input('Ingrese los números que desea sumar separados por un espacio: ').split(" ")  # Crea una lista con cada uno de los valores dados.
                resultado = aritmetica.sumar(elementos)
                print("Resultado de la suma: {}".format(resultado))
                outputs.escribir_archivo(modo.upper(), resultado)
            elif modo.lower() == 'resta':
                elementos = input('Ingrese el minuendo y el sustraendo, separados por un espacio: ').split(" ")
                resultado = aritmetica.restar(elementos)
                print("Resultado de la resta: {}".format(resultado))
                outputs.escribir_archivo(modo.upper(), resultado)
            elif modo.lower() == 'mult':
                elementos = input('Ingrese los números que desea multiplicar separados por un espacio: ').split(" ")
                resultado = aritmetica.multiplicar(elementos)
                print("Resultado del producto: {}".format(resultado))
                outputs.escribir_archivo(modo.upper(), resultado)
            elif modo.lower() == 'div':
                elementos = input('Ingrese el dividendo y el divisor, separados por un espacio: ').split(" ")
                resultado = aritmetica.dividir(elementos)
                print("Resultado de la división: {}".format(resultado))
                outputs.escribir_archivo(modo.upper(), resultado)
            elif modo.lower() == 'factorial':
                elemento = int(input('Ingrese el número entero que desea usar: '))
                resultado = aritmetica.calcular_factorial(elemento)
                print("El factorial de {} es: {}".format(elemento, resultado))
                outputs.escribir_archivo(modo.upper(), resultado)
            elif modo.lower() == 'potencia':
                elementos = input('Ingrese la base y el exponente separados por un espacio: ').split(" ")
                resultado = aritmetica.calcular_potencia(elementos)
                print("La potencia con base {} y exponente {} es: {}".format(elementos[0], elementos[1], resultado))
                outputs.escribir_archivo(modo.upper(), resultado)
        except ValueError:
            outputs.notificar_error_operaciones()
            continue