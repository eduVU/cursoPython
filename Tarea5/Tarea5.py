#-----------------------------------------------------------------------------------------
# 1. Función para eliminar repetidos (tarea 2, ejercicio 6).

# Casos de prueba para esta función.
lista_prueba = [1, 2, 3, 3, 2, 4, 6]
# lista_prueba = [3, 3, 3, 3, 3, 3, 3]


# Fuención original: recibe una lista, retorna una lista sin repetidos.
# En cada iteración se consulta si el valor del i-esimo elemento de la lista ya se encuentra en la lista sin duplicados.
# Si aún no está en la lista, el nuevo valor único se incluye en ella.
def eliminar_repetidos(lista):
    listaNueva = []
    for i in range(len(lista)):
        if lista[i] not in listaNueva:
            listaNueva.append(lista[i])
    return listaNueva

resultado_funcion1 = eliminar_repetidos(lista_prueba)
print(f"Ejercicio 1 - función:\n Lista original: {lista_prueba}\n Lista sin repetidos: {resultado_funcion1}\n")

# Función lambda: un uso de la sintaxis básica de lambda, llamando a la función y brindando la lista que se desea trabajar.
resultado = (lambda x: eliminar_repetidos(x))(lista_prueba)
print(f"Ejercicio 1 - lambda:\n Lista original: {lista_prueba}\n Lista sin repetidos: {resultado}\n")

# ------------------------------------------------------------------------------------------
# 2. Función para eliminar todas las apariciones de un elemento en una lista (tarea 4, ejercicio 3).

# Casos de prueba para esta función.
lista_prueba2 = [2, 45, "gato", 130, 457.6, "papaya", 45]
elemento_removido = 45

# lista_prueba2 = ['hola', 'adios', 42, 7, 'hola', '@', 'adios', 105]
# elemento_removido = 'hola'


# Función original: recibe una lista, crea una copia de ella y el ciclo elimina cada aparición del elemento recibido retorna la lista filtrada.
def eliminar_elemento(lista, elemento):
    lista2 = lista.copy()  # Decidí trabajar una copia de la lista para imprimir la orginal y la copia al final.
    # Se elimina el elemento las veces necesarias hasta que desaparezca.
    while elemento in lista2:
        lista2.remove(elemento)
    return lista2

resultado_funcion2 = eliminar_elemento(lista_prueba2, elemento_removido)
print(f"Ejercicio 2 - función:\n Lista original: {lista_prueba2}\n Elemento a remover: {elemento_removido}\n Lista filtrada: {resultado_funcion2}\n")

# Función lambda: el filtro admite en la nueva lista solo a los elementos que no son el elemento que se desea remover.
resultado2 = list(filter(lambda x: x != elemento_removido, lista_prueba2))
print(f"Ejercicio 2 - lambda:\n Lista original: {lista_prueba2}\n Elemento a remover: {elemento_removido}\n Lista filtrada: {resultado2}\n")

# -------------------------------------------------------------------------------------------
# 3. Esta función recibe un string y cuenta los números, letras y caracteres especiales que la componen (tarea 4, ejercicio 1).

# Casos de prueba para esta función.
palabras_prueba3 = ['4#jk68Ty^&l8pz', '#"Q25.@ab7gd', 'PalAbRa123', '^"~!!!']
# palabras_prueba3 = ['78sdsr##0^', '^^^33^yui', 'oracion', '3.1412']


# Función original: recibe una palabra, y crea un diccionario con el conteo de cada caracter de distinta categoría.
# Retorna el diccionario con los resultados.
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

resultado_funcion3 = []
for i in range(4):
    resultado_funcion3.append(contar_num_let_car(palabras_prueba3[i]))
print(f"Ejercicio 3 - función:\n{resultado_funcion3}\n")

# Función lambda: con el uso de map() se aplica la función a todos los strings de prueba a la vez.
resultado3 = list(map(contar_num_let_car, palabras_prueba3))
print(f"Ejercicio 3 - lambda:\n{resultado3}\n")

# -------------------------------------------------------------------------------------------
# 4. Esta función se encarga de realizar la resta de números (módulo aritmético de la tarea 3).

# Casos de prueba para esta función.
numeros_prueba4 = ["35", "17"]
# numeros_prueba4 = ["3", "79"]


# Esta función recibe una lista con strings. Rrealiza la conversión a enteros y la resta entre minuendo y sustraendo.
# Retorna el resultado obtenido.
def restar(valores):
    diferencia = int(valores[0]) - int(valores[1])
    return diferencia

resultado_funcion4 = restar(numeros_prueba4)
print(f"Ejercicio 4 - función:\n Resultado: {resultado_funcion4}\n")

# Función lambda: se utiliza el parámetro x para representar a los valores de la lista con números de prueba.
resultado4 = (lambda x: int(x[0]) - int(x[1]))(numeros_prueba4)
print(f"Ejercicio 4 - lambda:\n Resultado: {resultado4}\n")
