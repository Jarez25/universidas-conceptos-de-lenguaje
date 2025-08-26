pregunta = input('¿Cuál es tu edad? ')
edad = int(pregunta)

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# a este le podemos agregar un manejo de errorer basico(try catch)
# y tambien hacerlos con match case