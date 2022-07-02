from decorators.PersonajeDecorator import PersonajeDecorator
from Personajes.personaje import Personaje
import random


class AlterDecorator(PersonajeDecorator):
    def __init__(self, tipo_personaje: Personaje):
        super(AlterDecorator, self).__init__(tipo_personaje)
        self.personaje_decorado.ATK = self.personaje_decorado.ATK + 8
        self.personaje_decorado.SPD = self.personaje_decorado.SPD + 3
        self.personaje_decorado.DEF = self.personaje_decorado.DEF - 2

    def atacar(self):
        atacar_con_fuerza: int = random.randint(0, 1)
        if atacar_con_fuerza == 1:
            return self.personaje_decorado.ATK + 2
        else:
            return self.personaje_decorado.ATK - 2

    def recibir_ataque(self, daño: int):
        daño = daño - self.personaje_decorado.DEF
        self.personaje_decorado.LP -= daño

    def usar_item(self):
        if self.personaje_decorado.usar_item():
            self.items_disponibles -= 1

    def get_hp(self):
        return self.personaje_decorado.get_hp()
