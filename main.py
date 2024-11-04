#El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.

#Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

#si A ganó el set, o
#si B ganó el set, o
#si el set todavía no termina, o
#si el resultado es inválido (por ejemplo, 8-6 o 7-3).
#Desarrolle un programa que solucione el problema de Solarrabietas:

#Juegos ganados por A: 4
#Juegos ganados por B: 5
#Aun no termina
#Juegos ganados por A: 5
#Juegos ganados por B: 7
#Gano B
#Juegos ganados por A: 5
#Juegos ganados por B: 6
#Aun no termina
#Juegos ganados por A: 3
#Juegos ganados por B: 7
#Invalido
#Juegos ganados por A: 6
#Juegos ganados por B: 4
#Gano A

def evaluar_set(juegos_A, juegos_B):
    # Comprobar si el resultado es inválido
    if juegos_A < 0 or juegos_B < 0 or (juegos_A > 7 and juegos_B > 6) or (juegos_B > 7 and juegos_A > 6):
        return "Invalido"
    
    # Reglas del tenis para ganar un set
    if juegos_A >= 6 and (juegos_A - juegos_B) >= 2:
        return "Gano A"
    elif juegos_B >= 6 and (juegos_B - juegos_A) >= 2:
        return "Gano B"
    
    # Reglas para empate
    if juegos_A == 6 and juegos_B == 6:
        return "Aun no termina"
    
    # Si están empatados a 5
    if juegos_A == 5 and juegos_B == 5:
        return "Aun no termina"
    
    # Si se cumple la condición de que el set aún no ha terminado
    if juegos_A < 6 and juegos_B < 6:
        return "Aun no termina"
    
    # Si ninguna de las condiciones anteriores se cumple, se considera inválido
    return "Invalido"

# Ciclo para ingresar los resultados
while True:
    try:
        juegos_A = int(input("Juegos ganados por A: "))
        juegos_B = int(input("Juegos ganados por B: "))
        
        resultado = evaluar_set(juegos_A, juegos_B)
        print(resultado)

    except ValueError:
        print("Por favor, ingrese números válidos.")
    
    # Preguntar si desea continuar
    continuar = input("¿Desea ingresar otro resultado? (s/n): ")
    if continuar.lower() != 's':
        break
