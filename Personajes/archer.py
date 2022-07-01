from Personajes.personaje import Personaje


class Archer(Personaje):

    def __init__(self):
        self.LP: int = 100
        self.ATK: int = 28
        self.DEF: int = 15
        self.SPD: int = 15
        self.estado: bool = False
        self.items_disponibles: int = 3

    def atacar(self):
        pass

    def usar_item(self):
        if self.items_disponibles > 0:
            self.items_disponibles -= 1
            return True
        else:
            return False

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
