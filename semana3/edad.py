#Preguntar al usuario su edad y mostrar en pantalla todos los años que ha
#cumplido (desde 1 hasta su edad).

edad = int(input("¿Cuántos años tienes? "))

print(f"\nHas cumplido los siguientes años:")
for i in range(1, edad + 1):
    print(i)
