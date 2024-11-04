#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.

#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.
#Ingrese a: 3.9
#Ingrese b: 6.0
#Ingrese c: 1.2
#No es un triangulo valido.
#Ingrese a: 1.9
#Ingrese b: 2
#Ingrese c: 2
#El triangulo es isoceles.
#Ingrese a: 3.0
#Ingrese b: 5.0
#Ingrese c: 4.0
#El triangulo es escaleno.

def tipo_triangulo(a, b, c):
    # Verificar la desigualdad triangular
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo válido."
    
    # Determinar el tipo de triángulo
    if a == b == c:
        return "El triángulo es equilátero."
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles."
    else:
        return "El triángulo es escaleno."

# Solicitar los lados del triángulo
while True:
    try:
        a = float(input("Ingrese a: "))
        b = float(input("Ingrese b: "))
        c = float(input("Ingrese c: "))

        resultado = tipo_triangulo(a, b, c)
        print(resultado)

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
    
    # Preguntar si desea continuar
    continuar = input("¿Desea ingresar otro triángulo? (s/n): ")
    if continuar.lower() != 's':
        break
