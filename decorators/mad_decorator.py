from decorators.PersonajeDecorator import PersonajeDecorator
import random


class MadDecorator(PersonajeDecorator):
    def __init__(self):
        super.__init__()
        self.personaje_decorado.ATK = self.personaje_decorado.ATK * 2
        nueva_defensa = self.personaje_decorado.DEF % 2
        self.personaje_decorado.DEF = self.personaje_decorado.DEF / 2 + nueva_defensa
        self.guts_disponibles = 1

    def atacar(self):
        return self.personaje_decorado.ATK

    def recibir_ataque(self, daño: int):
        daño = daño - self.personaje_decorado.DEF
        self.personaje_decorado.LP -= daño
        if self.personaje_decorado.LP <= 0:
            guts: int = random.randint(0, 1)
            if guts == 1 and self.guts_disponibles != 0:
                self.personaje_decorado.LP = 1
                self.guts_disponibles -= 1

    def usar_item(self):
        self.personaje_decorado.usar_item()
