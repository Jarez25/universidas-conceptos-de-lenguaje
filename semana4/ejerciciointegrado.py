# 1. Función sin parámetros y sin retorno de valor
def mostrar_bienvenida():
    print("¡Bienvenido al sistema de registro de asistencia!")
# Esta función solo imprime un mensaje. No recibe datos ni devuelve nada.


# 2. Función sin parámetros y con retorno de valor
def obtener_nombre_clase():
    return "Conceptos de Lenguajes"
# Esta función retorna el nombre del curso. No necesita entrada de datos.


# 3. Función con parámetros y sin retorno de valor
def registrar_asistencia(nombre):
    print(f"{nombre} ha sido registrada como presente.")
# Esta función recibe el nombre del estudiante y muestra un mensaje. No retorna nada.


# 4. Función con parámetros y con retorno de valor
def generar_mensaje_asistencia(nombre, hora):
    return f"{nombre} llegó a clase a las {hora}."
# Esta función recibe dos datos y retorna un mensaje personalizado.


# 5. Ejecución del programa
mostrar_bienvenida()
print("Clase:", obtener_nombre_clase())

registrar_asistencia("Massiel")

mensaje = generar_mensaje_asistencia("Massiel", "6:30 P.M")
print(mensaje)
