#Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

#Ingrese un número: 4
#Su número es par
#Ingrese un número: 3
#Su número es impar


# Solicitar al usuario que ingrese un número
numero = int(input("Enter a number: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print("Its number is even")
else:
    print("Its number is odd")
