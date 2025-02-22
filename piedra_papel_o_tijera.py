
# Condicional
jugador_1 = input("jugador 1: ")
opcion_jugador_1 = input("piedra, papel o tijera: ")

jugador_2 = input("Jugador 2: ")
opcion_jugador_2 = input("piedra, papel o tijera: ")

print(jugador_1)
print(jugador_2)


# OPCIONES DE JUEGO
if(opcion_jugador_1 != "piedra" and opcion_jugador_1 != "papel" and opcion_jugador_1 != "tijera") or (opcion_jugador_2 != "piedra" and opcion_jugador_2 != "papel" and opcion_jugador_2 != "tijera"):
    print("opcion no valida")

else:
# opciones donde gana el jugador 1
    if (opcion_jugador_1 == "piedra") and (opcion_jugador_2 == "tijera"):
        print("jugador 1 gana con piedra")     #piedra vs tijera = gana piedra 

    elif (opcion_jugador_1 == "papel") and (opcion_jugador_2 == "piedra"):
        print("jugador 1 gana con papel")     #papel vs piedra = gana papel

    elif (opcion_jugador_1) == "tijera" and (opcion_jugador_2) == "papel":
        print("jugador 1 gana con tijera")     #tijera vs papel = gana tijera

    # opciones donde gana el jugardor 2

    elif (opcion_jugador_2 == "piedra") and (opcion_jugador_1 == "tijera"):
        print("jugador 2 gana con piedra")     #piedra vs tijera = gana piedra 

    elif (opcion_jugador_2 == "papel") and (opcion_jugador_1 == "piedra"):
        print("jugador 2 gana con papel")     #papel vs piedra = gana papel

    elif (opcion_jugador_2) == "tijera" and (opcion_jugador_1) == "papel":
        print("jugador 2 gana con tijera")     #tijera vs papel = gana tijera

    # opcion de empate

    elif (opcion_jugador_1) == (opcion_jugador_2):
        print("empate")             # Opciones iguales = empate

    else:
        print("opcion no valida")



