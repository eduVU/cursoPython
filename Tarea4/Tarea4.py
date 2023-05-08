"""
EJERCICIO 1: Esta función recibe un string y cuenta los números, letras
y caracteres especiales que la componen.
"""
def contar_num_let_car(palabra):
    # Este diccionario almacena los tres tipos de valores posibles.
    diccionario = {
        "Letras": 0,
        "Números": 0,
        "Caracteres especiales": 0
    }
    # Se verifica el tipo de caracter y se agrega al conteo del diccionario.
    for i in palabra:
        if i.isalpha() == True:
            diccionario["Letras"] += 1
        elif i.isdecimal() == True:
            diccionario["Números"] += 1
        else:
            diccionario["Caracteres especiales"] += 1
    return diccionario

"""
EJERCICIO 2: Esta función cuenta todas las veces que aparece cada caracter
dentro de un string dado y muestra los resultados en un diccionario.
Caracteres en mayúscula y minúscula son distintos para esta función.
"""
def contar_car_dicc(palabra):
    lista_unica = []  # Lista de control con los caracteres únicos de la palabra.
    diccionario = {}
    for i in palabra:
        if i not in lista_unica:  # Cada vez que un elemento sea único, se añade este y su cantidad al diccionario.
            lista_unica.append(i)
            diccionario[i] = palabra.count(i)
    return diccionario

"""
EJERCICIO 3: Esta función elimina todas las apariciones de un elemento
en una lista.
"""
def eliminar_elemento(lista, elemento):
    lista2 = lista.copy()  # Decidí trabajar una copia de la lista para imprimir la orginal y la copia al final.
    # Se elimina el elemento las veces necesarias hasta que desaparezca.
    while elemento in lista2:
        lista2.remove(elemento)
    return lista2

"""
EJERCICIO 4: Esta función recibe una secuencia de números separados
por coma e imprime una lista y una tupla con dichos valores.
"""
def crear_lista_tupla(secuencia):
    lista = secuencia.split(',')  # Los números son dados separados por coma.
    # Convertir los valores a enteros.
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    tupla = tuple(lista)
    return lista, tupla


# Algunos casos de prueba para cada ejercicio:
# EJERCICIO 1:

palabra_prueba1 = '4#jk68Ty^&l8pz'
# palabra_prueba1 = '#"Q25.@ab7gd'
# palabra_prueba1 = 'PalAbRa123'
# palabra_prueba1 = '^"~!!!'

resultado = contar_num_let_car(palabra_prueba1)
print("Ejercicio 1:\n Input: {}\nResultado:\n Letras = {}\n" 
    " Números = {}\n Caracteres especiales = {}".format(
        palabra_prueba1, resultado["Letras"], resultado["Números"], resultado["Caracteres especiales"]))


# EJERCICIO 2:

palabra_prueba2 = "azafata"
# palabra_prueba2 = "cuenta"
# palabra_prueba2 = "paralelepipedo"
# palabra_prueba2 = "AAayudaaa"

dicc_prueba2 = contar_car_dicc(palabra_prueba2)
print("Ejercicio 2:\n Input: {}\n Diccionario: {}"
    .format(palabra_prueba2, dicc_prueba2))


# EJERCICIO 3:

lista_prueba3 = [2, 45, "gato", 130, 457.6, "papaya", 45]
elemento_removido = 45

# lista_prueba3 = ['hola', 'adios', 42, 7, 'hola', '@', 'adios', 105]
# elemento_removido = 'hola'

# lista_prueba3 = [4, 4, 4, '@', 4, 4]
# elemento_removido = 4

# lista_prueba3 = ['todas', 'son', "distintas", 6, 'en', 'total']
# elemento_removido = 'nada'

lista_filtrada = eliminar_elemento(lista_prueba3, elemento_removido)
print("Ejercicio 3:\n Lista original: {}\n Elemento a remover: {}\n Lista filtrada: {}"
    .format(lista_prueba3, elemento_removido, lista_filtrada))


# EJERCICIO 4:

input_prueba4 = "6,5,4,3,2,1"  # Asumiendo que el input viene de la terminal, entonces sería un string.
# input_prueba4 = "1,1,3,4,78,89,45"
# input_prueba4 = "0,0,0,0,0,1,1,1,1,4,4,4,4"
# input_prueba4 = "1"

lista, tupla = crear_lista_tupla(input_prueba4)
print("Ejercicio 4:\n Input: {}\n Lista: {}\n Tupla: {}"
    .format(input_prueba4, lista, tupla))