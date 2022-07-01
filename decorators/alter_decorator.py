from decorators.PersonajeDecorator import PersonajeDecorator
import random


class AlterDecorator(PersonajeDecorator):
    def __init__(self):
        super.__init__()
        self.personaje_decorado.ATK = self.personaje_decorado + 8
        self.personaje_decorado.SPD = self.personaje_decorado.SPD + 3
        self.personaje_decorado.DEF = self.personaje_decorado.DEf - 2

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
        self.personaje_decorado.usar_item()
