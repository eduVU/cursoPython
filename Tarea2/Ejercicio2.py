# Ejercicio 2 - Triángulo de tamaño 'n'.

# Se verifica que se haya ingresado un número entero.
try:
    n = int(input('Ingrese un número entero mayor a cero para definir el tamaño del triángulo: '))
except ValueError:
    print('ERROR: el valor ingresado no es válido. Ingrese un número entero mayor a cero.')
    exit()
if n <= 0:  # Se descartan valores negativos o el cero como tamaño para el triángulo.
    print('ERROR: el valor ingresado no es válido. Ingrese un número entero mayor a cero.')
else:  # Se construye el triángulo para valores de n válidos.
    # La lista contiene los elementos que se ponen en la base tras cada iteración.
    base = []
    # Desde 1 hasta n, en cada iteración se agrega un número a la lista 'base' y se imprime el contenido de esta.
    for i in range(1, n+1):
        base.append(i)
        print(*base)