from decorators.PersonajeDecorator import PersonajeDecorator
from Personajes.personaje import Personaje
import random


class MaxDecorator(PersonajeDecorator):
    def __init__(self, tipo_personaje: Personaje):
        super(MaxDecorator, self).__init__(tipo_personaje)
        self.personaje_decorado.LP = 100
        self.personaje_decorado.ATK = self.personaje_decorado.ATK - 5

    def atacar(self):
        return self.personaje_decorado.ATK

    def recibir_ataque(self, daño: int):
        daño = daño - self.personaje_decorado.DEF
        reducir_daño: int = random.randint(0, 1)
        if reducir_daño == 1:
            self.personaje_decorado.LP = self.personaje_decorado.LP - (daño/2)

    def usar_item(self):
        if self.personaje_decorado.usar_item():
            self.items_disponibles -= 1

    def get_hp(self):
        return self.personaje_decorado.get_hp()
