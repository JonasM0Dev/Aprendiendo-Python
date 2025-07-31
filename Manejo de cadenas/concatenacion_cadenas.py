#Concatenacion de cadenas

#1. Concatenación simple con +
cadena_1 = "Hola"
cadena_2 = "Mundo"

concatenacion = cadena_1 + " " + cadena_2
print (concatenacion) #Salida: Hola Mundo

#2. Concatenación con números (usando str())
nombre = "Ana"
edad = 25 
print (f"{nombre} tiene {str(edad)} años") #Salida: Ana tiene 25 años

#3. Uso de .format()
producto = "laptop"
precio = 1200
resultado = "La {} cuesta {}".format(producto, precio)
print (resultado) #Salida: La laptop cuesta 1200

#4. f-strings (formato moderno)
ciudad = "Madrid"
temperatura = 28.5
resultado = f"La temperaura en {ciudad} es de {temperatura} °C"
print (resultado) #°C" #Salida: La temperatura en Madrid es de 28.5 °C

#5. Concatenación con listas usando join()
frutas = ["manzana", "pera", "uva", "naranja"] #Lo que esta dentro de [] es una lista
resultado = ", ".join(frutas)
print (resultado) #Salida: manzana, pera, uva, naranja 

#6. Multiplicación de cadenas
palabra = "Pyhton " #Dejo un espacion para que sea mas legible en la salida
resultado = palabra * 5
print (resultado) #Salida: Python Python Python Python

#7. Concatenación en un bucle
letras = ["A", "B", "C", "D"] #Otra vez listas
resultado = ""
for letra in letras: #Bucle for
    resultado += letra + "-"
print (resultado) #Salida: A-B-C-D-

#8. Eliminar espacios y concatenar
texto = "  Hola   "
nombre = " mundo"
resultado =texto.strip() + nombre
print (resultado) #Salida: Hola mundo

#9. Concatenación con saltos de línea
linea1 = "Primer salto de linea"
linea2 = "Segundo salto de linea"
resultado = linea1 + "\n" + linea2
print (resultado) #Salida: # Primera línea
                           # Segunda línea