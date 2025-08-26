nota = int(input("Ingrese su nota: "))

if nota < 60 and nota >= 0:
    print("Usted reprobó la clase")
elif nota >= 60 and nota <= 100:
    print("Usted aprobó la clase")
else:
    print("La nota que ingresó no es válida")
