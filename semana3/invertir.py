# Preguntar al usuario una cantidad a invertir, el interés anual y el número de
# años, y muestre por pantalla el capital obtenido en la inversión cada año
# que dura la inversión. – Monto por año = (1 + interés/100)

monto_inicial = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (en %): "))
años = int(input("Ingrese el número de años: "))

capital = monto_inicial

print("\nCapital al final de cada año:")


for año in range(1, años + 1):
    capital = capital * (1 + interes_anual / 100)
    print(f"Año {año}: {capital:.2f}")
