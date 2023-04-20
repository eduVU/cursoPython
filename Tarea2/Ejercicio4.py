# Ejercicio 4 - Lista al cubo.

# Para efectos prácticos, se limitan los números aleatorios de la siguiente forma:
# Cantidad de elementos de una lista aleatoria: de 1 a 100.
# Posibles valores para cada uno de los elementos de una lista: de 0 a 1000.

import random  # Librería para generar números aleatorios.
lista = []  # Se inicializa la lista que tendrá los elementos originales.
cubos = []  # Se inicializa la lista que tendrá el cubo de los elementos originales.
cantidad = input('Ingrese la cantidad de valores de la lista o la palabra'
    ' \'random\' para generar una lista entre 1 y 100 valores: ')
if cantidad == 'random':
    tamano = random.randint(1,100)  # Se escoge al azar el tamaño de la lista.
else:
    # Primero se comprueba que el número de valores de la lista sea un número entero.
    try:
        tamano = int(cantidad)
    except ValueError:
        print('ERROR: la cantidad de valores de la lista debe ser un número entero positivo.')
        exit()
    # Luego se comprueba que el tamaño de la lista sea un entero mayor a cero.
if tamano <= 0:
    print('ERROR: la cantidad de valores de la lista debe ser un número entero positivo.')
    exit()
else:
    # Se llenan las listas con valores aleatorios acorde a su tamaño.
    for i in range(tamano):
        lista.append(random.randint(0,1000))
        cubos.append(lista[i]**3)  # Se calcula el cubo para cada valor de la lista.
    print(lista)
    print(cubos)