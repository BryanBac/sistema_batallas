from abc import ABCMeta, abstractmethod
from Personajes.personaje import Personaje


class PersonajeDecorator(metaclass=ABCMeta):
    def __init__(self, tipo_personaje: Personaje):
        self.cantidad_items: int = 0
        self.personaje_decorado: Personaje = tipo_personaje
        self.items_disponibles = self.personaje_decorado.items_disponibles

    @abstractmethod
    def atacar(self):
        raise NotImplementedError

    @abstractmethod
    def recibir_ataque(self, daño: int):
        raise NotImplementedError

    @abstractmethod
    def usar_item(self):
        raise NotImplementedError

    @abstractmethod
    def get_hp(self):
        raise NotImplementedError
