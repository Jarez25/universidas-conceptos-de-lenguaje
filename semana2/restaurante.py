consumo = float(input("Ingrese el valor de consumo: "))

iva = consumo * 0.15
propina = consumo * 0.10
total = consumo + iva + propina

print("\nFACTURA RESTAURANTE")
print(f"Consumo: {consumo:.2f}")
print(f"IVA (15%): {iva:.2f}")
print(f"Propina (10%): {propina:.2f}")
print(f"Total a Pagar: {total:.2f}")
