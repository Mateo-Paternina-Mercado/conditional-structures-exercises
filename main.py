
#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.
#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.
#Palabra 1: sol
#Palabra 2: paralelepipedo
#La palabra paralelepipedo tiene 11 letras mas que sol
#Palabra 1: plancha
#Palabra 2: lapices
#Las dos palabras tienen el mismo largo

# Solicitar al usuario que ingrese dos palabras
palabra1 = input("word 1: ")
palabra2 = input("word 2: ")

# Calcular la longitud de ambas palabras
longitud1 = len(palabra1)
longitud2 = len(palabra2)

# Comparar las longitudes y mostrar el resultado
if longitud1 > longitud2:
    diferencia = longitud1 - longitud2
    print(f"the word {palabra1} has {diferencia} letters more than {palabra2}.")
elif longitud2 > longitud1:
    diferencia = longitud2 - longitud1
    print(f"the word {palabra2} has {diferencia} letters more than {palabra1}.")
else:
    print("The two words are the same length.")
