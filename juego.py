from Personajes.personaje import Personaje
from Personajes.archer import Archer
from Personajes.assassin import Assassin
from Personajes.lancer import Lancer
from Personajes.saber import Saber


p1: Personaje
p2: Personaje
opcion: int = 1

while opcion != 2:
    agregar: str = ""
    print("####### Menu #######\n")
    print("1. ¡ Jugar !")
    print("2. Salir\n")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("\n----------- Personajes ----------\n")
        print("1. Archer")
        print("2. Assassin")
        print("3. Lancer")
        print("4. Saber")
        opJugador: int = int(input("\nJugador 1, seleccione un personaje: "))

        if opJugador == 1:
            p1 = Archer()

        elif opJugador == 2:
            p1 = Assassin()

        elif opJugador == 3:
            p1 = Lancer()

        elif opJugador == 4:
            p1 = Saber()

        opJugador2: int = int(input("\nJugador 2, seleccione un personaje: "))

        if opJugador2 == 1:
            p2 = Archer()

        elif opJugador2 == 2:
            p2 = Assassin()

        elif opJugador2 == 3:
            p2 = Lancer()

        elif opJugador2 == 4:
            p2 = Saber()

        print("¡ PELEEN !")
