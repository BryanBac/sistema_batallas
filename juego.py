from Personajes.personaje import Personaje
from Personajes.archer import Archer
from Personajes.assassin import Assassin
from Personajes.lancer import Lancer
from Personajes.saber import Saber
from decorators.PersonajeDecorator import PersonajeDecorator
from decorators.mad_decorator import MadDecorator
from decorators.max_decorator import MaxDecorator
from decorators.alter_decorator import AlterDecorator
from decorators.light_decorator import LightDecorator
from decorators.heal_decorator import HealDecorator
from decorators.stun_decorator import StunDecorator


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
        batalla: int = 0
        turno = 1
        while batalla != 4:
            print(f"\n----------- Jugador {turno}----------\n")
            print("1. Atacar")
            print("2. Mejorar")
            print("3. Pasar")
            batalla = int(input("Seleccione su opcion: "))
            if batalla == 1:
                if turno == 1:
                    if p1.items_disponibles == 3:
                        p2.recibir_danio(p1.atacar())
                    else:
                        p2.recibir_ataque(p1.atacar())
                if turno == 2:
                    if p1.items_disponibles == 3:
                        p1.recibir_danio(p2.atacar())
                    else:
                        p1.recibir_ataque(p2.atacar())
                if p1.get_hp() <= 0:
                    print("Gana jugador 2")
                    batalla = 4
                elif p2.get_hp() <= 0:
                    print("Gana jugador 1")
                    batalla = 4
            elif batalla == 2:
                print("\n----------- Seleccione opcion de cambio----------\n")
                print("1. Alter")
                print("2. Heal")
                print("3. Velocidad")
                print("4. Locura")
                print("5. Maximo HP")
                print("6. Paralizar")
                eleccion: int = int(input("Seleccione su opcion: "))
                if turno == 1:
                    if eleccion == 1:
                        p1 = AlterDecorator(p1)
                    elif eleccion == 2:
                        p1 = HealDecorator(p1)
                    elif eleccion == 3:
                        p1 = LightDecorator(p1)
                    elif eleccion == 4:
                        p1 = MadDecorator(p1)
                    elif eleccion == 5:
                        p1 = MaxDecorator(p1)
                    else:
                        p1 = StunDecorator(p1)
                    p1.usar_item()
                elif turno == 2:
                    if eleccion == 1:
                        p2 = AlterDecorator(p2)
                    elif eleccion == 2:
                        p2 = HealDecorator(p2)
                    elif eleccion == 3:
                        p2 = LightDecorator(p2)
                    elif eleccion == 4:
                        p2 = MadDecorator(p2)
                    elif eleccion == 5:
                        p2 = MaxDecorator(p2)
                    else:
                        p2 = StunDecorator(p2)
                    p2.usar_item()
            elif batalla == 3:
                print(f"Paso, te toca jugador {turno}")
            if turno == 1:
                turno = 2
            else:
                turno = 1
