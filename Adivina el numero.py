import random

def jugar_adivinanza():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento_usuario = int(input("Introduce tu intento: "))
        intentos += 1

        if intento_usuario < numero_aleatorio:
            print("El número que estoy pensando es mayor que", intento_usuario, ". Intenta de nuevo.")
        elif intento_usuario > numero_aleatorio:
            print("El número que estoy pensando es menor que", intento_usuario, ". Intenta de nuevo.")
        else:
            print("¡Felicidades! ¡Has adivinado el número en", intentos, "intentos!")
            break

jugar_adivinanza()