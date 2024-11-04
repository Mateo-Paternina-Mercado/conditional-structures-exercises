#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.
#La salida del programa debe ser el resultado de la operación.
#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5
#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1
#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20
#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5
#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1

# Función para realizar la operación
def calculadora(operando1, operador, operando2):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        if operando2 != 0:
            return operando1 / operando2
        else:
            return "Error: División por cero"
    elif operador == '**':
        return operando1 ** operando2
    else:
        return "Operador no válido"

# Solicitar entradas al usuario
while True:
    try:
        operando1 = float(input("Operating: "))
        operador = input("Operator: ")
        operando2 = float(input("Operating: "))

        resultado = calculadora(operando1, operador, operando2)

        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"{operando1} {operador} {operando2} = {resultado}")

    except ValueError:
        print("Please enter valid numbers.")

    # Preguntar si desea continuar
    continuar = input("Do you want to perform another operation? (s/n): ")
    if continuar.lower() != 's':
        break
