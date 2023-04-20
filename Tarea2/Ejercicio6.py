# Ejercicio 6 - Eliminar repetidos.

# El punto de partida es una lista cualquiera, aquí se brindan algunos ejemplos (descomentar solo una a la vez):
lista = [1, 2, 3, 3, 2, 4, 6]
# lista = [3, 3, 3, 3, 3, 3, 3]
# lista = [1, 2, 3, 5, 6]
# lista = [0, 2, 3, 5, 6, 0, 5, 1, 1, 2]
# lista = [2, 2, 3, 3, 1, 1, 0, 2]

# Se inicializa la nueva lista sin duplicados.
listaNueva = []  

# En cada iteración se consulta si el valor del i-esimo elemento de la lista ya se encuentra en la lista sin duplicados.
for i in range(len(lista)):
    condicion = lista[i] in listaNueva
    # Si el valor del i-esimo elemento aún no está en la nueva lista, se agrega.
    if condicion == False:
        listaNueva.append(lista[i])
print(listaNueva)