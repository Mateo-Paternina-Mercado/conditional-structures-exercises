#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.
#Ingrese caracter: 9
#Es numero.
#Ingrese caracter: A
#Es letra mayúscula.
#Ingrese caracter: f
#Es letra minúscula.
#Ingrese caracter: #
#No es letra ni número.

# Solicitar al usuario que ingrese un carácter
caracter = input("Enter character: ")

# Verificar si el carácter es una letra
if caracter.isalpha():
    if caracter.isupper():
        print("It is capital letter.")
    else:
        print("It is lowercase letter.")
# Verificar si el carácter es un número
elif caracter.isdigit():
    print("It is number.")
# Si no es ni letra ni número
else:
    print("It is not a letter or number.")
