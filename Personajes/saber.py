from Personajes.personaje import Personaje


class Saber(Personaje):

    def __init__(self):
        self.LP: int = 100
        self.ATK: int = 36
        self.DEF: int = 14
        self.SPD: int = 15
        self.estado: bool = False
        self.items_disponibles: int = 3

    def atacar(self):
        return self.ATK

    def usar_item(self):
        if self.items_disponibles > 0:
            self.items_disponibles -= 1
            return True
        else:
            return False

    def recibir_ataque(self, daño: int):
        daño_total: int = daño - self.DEF
        if daño_total > 0:
            self.LP -= daño_total
        else:
            print("El personaje tieme mejor defensa que su ataque")

    def get_spd(self):
        return self.SPD

    def get_hp(self):
        return self.LP

    def get_def(self):
        return self.DEF
