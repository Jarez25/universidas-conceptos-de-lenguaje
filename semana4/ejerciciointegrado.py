def mostrar_bienvenida():
    print("¡Bienvenido al sistema de registro de asistencia!")


def obtener_nombre_clase():
    return "Conceptos de Lenguajes"


def registrar_asistencia(nombre):
    print(f"{nombre} ha sido registrada como presente.")


def generar_mensaje_asistencia(nombre, hora):
    return f"{nombre} llegó a clase a las {hora}."


mostrar_bienvenida()
print("Clase:", obtener_nombre_clase())
