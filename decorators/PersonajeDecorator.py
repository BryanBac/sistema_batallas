from abc import ABCMeta, abstractmethod


class PersonajeDecorator(metaclass=ABCMeta):
    def __init__(self):
        self.cantidad_items: int = 0

    @abstractmethod
    def atacar(self):
        raise NotImplementedError

    @abstractmethod
    def recibir_ataque(self):
        raise NotImplementedError

    @abstractmethod
    def usar_item(self):
        raise NotImplementedError
