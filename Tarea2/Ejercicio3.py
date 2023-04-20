# Ejercicio 3 - Strings intercaladas.

# Se reciben ambas palabras.
string1 = input('Ingrese la primera palabra a intercalar: ')
string2 = input('Ingrese la segunda palabra a intercalar: ')

# Se comprueba que ambas palabras tengan el mismo largo.
if len(string1) != len(string2):
    print('Error: no se pueden intercalar las palabras, una es más larga que la otra.')
    exit()
else:
    resultado = ''  # Se inicializa la palabra resultante.
    # Se agregan los caracteres intercalados de las palabras iniciales para conformar la palabra resultante.
    for i in range (len(string1)):
        resultado = resultado + string1[i] + string2[i]
    print(resultado)