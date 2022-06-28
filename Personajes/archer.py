from Personajes.personaje import Personaje


class Archer(Personaje):

    def __init__(self):
        self.LP: int = 100
        self.ATK: int = 14
        self.DEF: int = 25
        self.SPD: int = 15
        self.estado: bool = False

    def atacar(self):
        pass

    def usar_item(self):
        pass

    def recibir_danio(self):
        pass

    def get_atk(self):
        pass

    def get_spd(self):
        pass

    def get_hp(self):
        pass

    def get_def(self):
        pass
