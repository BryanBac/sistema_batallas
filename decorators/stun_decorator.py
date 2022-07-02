from decorators.PersonajeDecorator import PersonajeDecorator
from Personajes.personaje import Personaje


class StunDecorator(PersonajeDecorator):
    def __init__(self, tipo_personaje: Personaje):
        super(StunDecorator, self).__init__(tipo_personaje)
        self.personaje_decorado.estado = True

    def atacar(self):
        if self.personaje_decorado.estado:
            self.personaje_decorado.estado = False
            return 0
        else:
            return self.personaje_decorado.ATK

    def recibir_ataque(self, daño: int):
        daño = daño - self.personaje_decorado.DEF
        self.personaje_decorado.LP -= daño

    def usar_item(self):
        if self.personaje_decorado.usar_item():
            self.items_disponibles -= 1

    def get_hp(self):
        return self.personaje_decorado.get_hp()
