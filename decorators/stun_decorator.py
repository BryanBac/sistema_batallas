from decorators.PersonajeDecorator import PersonajeDecorator


class StunDecorator(PersonajeDecorator):
    def __init__(self):
        super.__init__()
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
        self.personaje_decorado.usar_item()
