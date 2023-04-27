# Intecalar strings.
def intercalar(string1, string2):
    resultado = ''  # Se inicializa la palabra resultante.
    if len(string1) != len(string2):
        print('Error: no se pueden intercalar las palabras, una es más larga que la otra.')
    else:
    # Se agregan los caracteres intercalados de las palabras iniciales para conformar la palabra resultante.
        for i in range (len(string1)):
            resultado = resultado + string1[i] + string2[i]
    return resultado

# Convertir todo a mayúscula.
def mayuscula(string1, string2):
    mayus1 = string1.upper()
    mayus2 = string2.upper()
    return mayus1, mayus2

# Convertir todo a minúscula.
def minuscula(string1, string2):
    minus1 = string1.lower()
    minus2 = string2.lower()
    return minus1, minus2