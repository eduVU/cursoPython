""" Este módulo se encarga de las operaciones matemáticas de la calculadora: suma, resta, multiplicación, división, factorial y potencia.
Los resultados se entregan al módulo principal según corresponda.
"""

# Esta función se encarga de realizar la suma de n números.
def sumar(valores):
    sumatoria = 0
    for i in range(len(valores)):
        sumatoria += int(valores[i])  # Suma todos los valores de la lista.
    return sumatoria

# Esta función realiza la resta entre minuendo y sustraendo.
def restar(valores):
    if len(valores) != 2:  # Comprueba que se hayan recibido exactamente dos números, si no da un error.
        raise ValueError
    diferencia = int(valores[0]) - int(valores[1])
    return diferencia

# Esta función se encarga de realizar la multiplicación de n números.
def multiplicar(valores):
    producto = 1
    for i in range(len(valores)):
        producto = producto * int(valores[i])
    return producto

# Esta función se encarga de realizar la división entre dos números enteros.
def dividir(valores):
    if len(valores) != 2:  # Comprueba que se hayan recibido exactamente dos números, si no da un error.
        raise ValueError
    elif int(valores[1]) == 0:  # En caso de que el divisor sea cero da un error.
        raise ValueError
    else:
        cociente = int(valores[0])/int(valores[1])
        return cociente

# Esta función calcula el factorial de un número entero dado.
def calcular_factorial(n):
    factorial = 1  # Se inicializa la variable con el valor cuando n=0.
    if n < 0:  # Se verifica que n no sea negativo.
        raise ValueError
    elif n == 0:  # Se comprueba si n=0, en ese caso 0!=1.
        return factorial
    else:  # Se calcula n! para el resto de casos.
        # En cada iteración se multiplica el valor actual de 'factorial' por 'i'.
        for i in range(1, n+1):
            factorial = factorial*i
        return factorial
    
# Esta función calcula una potencia dada una base y un exponente.
def calcular_potencia(valores):
    if len(valores) != 2:  # Comprueba que se hayan recibido exactamente dos números, si no da un error.
        raise ValueError
    elif int(valores[0]) == 0 and int(valores[1]) == 0:  # Si la potencia es 0**0 da un error.
        raise ValueError
    else:
        potencia = int(valores[0])**int(valores[1])
        return potencia