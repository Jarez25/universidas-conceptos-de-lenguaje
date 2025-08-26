colores = ["rojo", "amarillo", "verde", "azul"]
print(colores) #['rojo', 'amarillo', 'verde', 'azul']
print(colores[1]) #amarillo
colores[0] = "rosado"
del colores[2]
colores.append("negro")
print(colores)#['rosado', 'amarillo', 'azul', 'negro']
colores.insert(0, "anaranjado")
print(colores) #['anaranjado', 'rosado', 'amarillo', 'azul', 'negro']


#aparte de estos estan append : que agrega el elemento al final
colores.append("azul")
print(colores)

#tambien tenesmo pos que agregar el datos en una parte expecifical del array
# nota recordemos que los valores del array inician en 0
colores.insert(1, "dorado")
print(colores)

# este sumar los array y los convierte en uno solo
colores.extend(["super rosa", "super blanco"])
print(colores)

# con solo elimina el ultimo dato de nuestro array
colores.pop()
print(colores)

# al darle un valor elimina el valor equivalente
# nota recordemos que los valores del array inician en 0 entonces el eliminaco es el dorado
colores.pop(1)
print(colores)

#elimina el primer valor que tenga ese nombre en este caso el primer azul
colores.remove("azul")
print(colores)

#elimina todos los datos del array
colores.clear()
print(colores)
