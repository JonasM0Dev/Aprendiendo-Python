#Reemplazar subcadenas

texto = "Hola, mundo"
nuevo_texto = texto.replace("mundo", "a todos")
print (nuevo_texto)

#Ejercicios de práctica sobre limpieza y reemplazo de texto

#NIVEL BASICO
#1. Censurado simple:
#Dado un texto con la palabra "spoiler", reemplázala por "*****".

texto = "spoiler"
nuevo_texto = texto.replace("spoiler", "*****")
print (nuevo_texto)

#Espacios molestos
#Elimina todos los guiones - de la siguiente cadena: "Teléfono: 123-456-7890".

texto = "Teléfono: 123-456-7890"
nuevo_texto = texto.replace("-", " ")
print (nuevo_texto)

#Reescribe un saludo
#Reemplaza "Hola, mundo" por "¡Buenos días, Python!".

texto = "Hola, mundo"
nuevo_texto = texto.replace("Hola", "¡Buenos dias").replace("mundo", "Python!")
print(nuevo_texto)

#NIVEL INTERMEDIO
#Corrección ortográfica automática
#Dado el texto "El cliemte compró un prodcuto defectuoso", corrige automáticamente las palabras mal escritas.

texto = "El cliemte compró un prodcuto defectuoso"
correciones = {"cliemte": "cliente",
               "prodcuto": "producto"}

for error, correcion in correciones.items():
    texto = texto.replace(error,correcion)
print (texto)

#Plantilla personalizada
#Tienes esta plantilla:
#"Hola {nombre}, gracias por tu compra en {tienda}."
#Reemplaza {nombre} y {tienda} con valores reales.

plantilla = "Hola {nombre}, gracias por tu compra en {tienda}."

texto = plantilla.format(nombre="Carlos", tienda="PythonhHub")
print (texto)

#Ejercicio: Confirmación de reserva
#Imagina que estás programando un sistema que envía correos de confirmación cuando alguien reserva una habitación de hotel. Tienes esta plantilla de mensaje:
#Hola {nombre}, tu reserva en el hotel {hotel} ha sido confirmada para el día {fecha}. Tu número de habitación es {habitacion}.

plantilla = """Hola {nombre}, tu reserva en el hotel {hotel} ha sido \
confirmada para el día {fecha}. Tu número de habitación es {habitacion}."""

datos = {
    "nombre": "Carlos",
    "hotel": "La torre",
    "fecha": "02/04/25",
    "habitacion": "325"
}

texto = plantilla.format(**datos)
print (texto)

#Texto limpio para análisis
#Dado un párrafo lleno de signos de puntuación innecesarios como ¡, !, ..., etc., reemplázalos o elimínalos dejando solo letras y espacios.

plantilla = "¡¡¡Hola!!! ¿Cómo estás...? Espero que... estés bien... 🤔 jeje! ¡Nos vemos pronto!!! 😉"

texto = plantilla.replace("¡","").replace("!","").replace("¿","").replace("?","").replace("...","")
print(texto)