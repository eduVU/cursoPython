# Ejercicio 1 - Factorial de un número dado.

factorial = 1  # Se inicializa la variable con el valor cuando n=0.

# Se verifica si se ingresa un valor no numérico.
try:
    n = int(input('Ingrese un número entero positivo: '))
except ValueError:
    print('ERROR: el valor ingresado no es válido. Ingrese un número entero positivo.')
    exit()
if n < 0:  # Se verifica que n no sea negativo.
    print('ERROR: el valor ingresado no es válido. Ingrese un número entero positivo.')
elif n == 0:  # Se comprueba si n=0, en ese caso 0!=1.
    print('El factorial de {} es {}.'.format(n, factorial))
else:  # Se calcula n! para el resto de casos.
    # En cada iteración se multiplica el valor actual de 'factorial' por 'i'.
    for i in range(1, n+1):
        factorial = factorial*i
    print('El factorial de {} es {}.'.format(n, factorial))