from decorators.PersonajeDecorator import PersonajeDecorator
import random


class LightDecorator(PersonajeDecorator):
    def __init__(self):
        super.__init__()
        self.personaje_decorado.SPD = self.personaje_decorado.SPD + 6
        self.personaje_decorado.DEF = self.personaje_decorado.DEF - 3

    def atacar(self):
        return self.personaje_decorado.ATK

    def recibir_ataque(self, daño: int):
        daño = daño - self.personaje_decorado.DEF
        le_dio: int = random.randint(0, 1)
        if le_dio == 1:
            self.personaje_decorado.LP -= daño

    def usar_item(self):
        self.personaje_decorado.usar_item()
