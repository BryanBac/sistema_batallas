from decorators.PersonajeDecorator import PersonajeDecorator


class MadDecorator(PersonajeDecorator):
    def __init__(self):
        super.__init__()

    def atacar(self):
        pass

    def recibir_ataque(self):
        pass

    def usar_item(self):
        pass
