#Convertir de cadena a numero

cadena1 = "10"
cadena2 = "5"
numero1 = int (cadena1)
numero2 = int (cadena2)
print (f"Convertir cadenas de '10' y '5' a entero: {numero1 + numero2}")

#Convertir de cadena a flotante
print ("-" * 40)
cadena = "5.16"
numero = float(cadena)
print (f"Convertir cadena de '5.16' a flotante: {numero + 1}")

#Convertir de numero a cadena
print ("-" * 40)
numero = 10
cadena = str(numero)
print (f"Converitr de numero '10' a cadena: {cadena}")

#Convertir a booleano
print ("-" * 40)
numero1 = 0
numero2 = 1
booleano1 = bool(numero1)
booleano2 = bool(numero2)
print (f"Convertir de numero '0' a booleano: {booleano1}")
print (f"Convertir de numero '1' a booleano: {booleano2}")

cadena = ""
booleano = bool(cadena)
print(f"Convertir de cadena a booleano: {booleano}")

cadena = "Texto de prueba"
booleano = bool(cadena)
print(f"Convertir de cadena a booleano: {booleano}")

variable = None
booleano = bool(variable)
print (f"Convertir de variable con 'None' a booleano: {booleano}")