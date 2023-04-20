# Ejercicio 5 - Notas de clase.

# Diccionario proporcionado para este ejercicio.
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80,
                "math": 90
            }
        }
    }
}

# Se calcula el promedio de las notas.
promedio = sampleDict["class"]["student"]["marks"]["physics"] + sampleDict["class"]["student"]["marks"]["history"] + sampleDict["class"]["student"]["marks"]["math"]
promedio = promedio/3

# Se crea un nuevo diccionario a partir de los datos de interés.
promedios = {
    "nombre": sampleDict["class"]["student"]["name"],
    "nota": promedio
}
print(promedios)