def calcular_imc(peso, estatura):
    """Calcula el índice de masa corporal (IMC)."""
    return peso / (estatura ** 2)

def evaluar_riesgo(edad, imc):
    """Evalúa la condición de riesgo según la edad y el IMC."""
    if edad < 45:
        if imc < 22.0:
            return "Riesgo bajo"
        else:
            return "Riesgo medio"
    else:
        if imc < 22.0:
            return "Riesgo medio"
        else:
            return "Riesgo alto"

# Solicitar entradas al usuario
try:
    estatura = float(input("Ingrese su estatura en metros: "))
    peso = float(input("Ingrese su peso en kilos: "))
    edad = int(input("Ingrese su edad: "))

    # Calcular el IMC
    imc = calcular_imc(peso, estatura)
    
    # Evaluar el riesgo
    riesgo = evaluar_riesgo(edad, imc)
    
    # Mostrar el resultado
    print(f"Su IMC es: {imc:.2f}")
    print(f"Condición de riesgo: {riesgo}")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
