## Notas sobre esta versión del código:

Actualmente, el código realiza todas las operaciones matemáticas, pero no escribe los resultados en un archivo.
El menú de ayuda y la opción de salir se despliegan en el menú principal, tal y como se espera.
Se captan los errores de typo de datos adecuadamente, pero algunos errores dentro de cada operación no se están procesando como se debe (i.e: la división entre cero se reporta como error, pero igual se realiza y retorna un None)

En resumen, queda por hacer:

- Manejo de errores para todas las operaciones.
- Escritura del archivo luego de cada operación.