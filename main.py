#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

#Dividendo: 14
#Divisor: 5
#La división no es exacta.
#Cociente: 2
#Resto: 4

#Dividendo: 100
#Divisor: 10
#La división es exacta.
#Cociente: 10
#Resto: 0

# Solicitar al usuario que ingrese el dividendo y el divisor
dividendo = int(input("Dividend: "))
divisor = int(input("Divider: "))

# Calcular el cociente y el resto
cociente = dividendo // divisor
resto = dividendo % divisor

# Determinar si la división es exacta
if resto == 0:
    print("The division is exact.")
else:
    print("The division is not exact.")

# Mostrar el cociente y el resto
print(f"Quotient: {cociente}")
print(f"Rest: {resto}")
