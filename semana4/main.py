# main.py
# from ejerciciointegrado import mostrar_bienvenida, obtener_nombre_clase, registrar_asistencia, generar_mensaje_asistencia
from ejerciciointegrado import *

# Llamado de las funciones
mostrar_bienvenida()
print("Clase:", obtener_nombre_clase())

registrar_asistencia("Massiel")

mensaje = generar_mensaje_asistencia("Massiel", "6:30 P.M")
print(mensaje)
