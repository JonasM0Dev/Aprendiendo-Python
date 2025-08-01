import os
os.system("cls")
#Metodos de cadenas

texto1 = "Hola Python"
texto2 = "straße" #Significa "Calle" en aleman. La letra "ß" esta en mayuscula
print (f"Texto original: {texto1}")

print (f"Texto con \".capitalize()\": {texto1.capitalize()}") #Solo deja la primera letra en mayuscula
print (f"Texto con \".lower()\": {texto1.lower()}") #Todo el texto queda en minusculas
print (f"Texto con \".casefold()\": {texto2.casefold()}") #Es parecido a ".lower()" pero mucho mas agresivo ya que no discrimina el alfabeto sin importar el idioma y lo hace minusculas
print (f"Texto con \".upper()\": {texto1.upper()}") #Todo el texto queda en mayusculas
print (f"Texto con \".title()\": {texto1.title()}") #Las primeras letras de cada palabra las hace mayuscula
print (f"Texto con \".swapcase()\": {texto1.swapcase()}") #Inviente las letras mayusculas por minusculas y viceversa