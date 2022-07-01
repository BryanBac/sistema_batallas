from decorators.PersonajeDecorator import PersonajeDecorator
import random


class HealDecorator(PersonajeDecorator):
    def __init__(self):
        super.__init__()
        self.personaje_decorado.LP = self.personaje_decorado.LP + 30
        self.personaje_decorado.DEF = self.personaje_decorado.DEF + 6

    def atacar(self):
        return self.personaje_decorado.ATK

    def recibir_ataque(self, daño: int):
        daño = daño - self.personaje_decorado.DEF
        self.personaje_decorado.LP -= daño
        if self.personaje_decorado.LP > 0:
            sanar: int = random.randint(0, 1)
            if sanar == 1:
                self.personaje_decorado.LP = self.personaje_decorado.LP + (daño/2)

    def usar_item(self):
        self.personaje_decorado.usar_item()
