from abc import ABCMeta, abstractmethod


class Personaje(metaclass=ABCMeta):

    @abstractmethod
    def atacar(self):
        raise NotImplementedError

    @abstractmethod
    def usar_item(self):
        raise NotImplementedError

    @abstractmethod
    def recibir_ataque(self, daño: int):
        raise NotImplementedError

    @abstractmethod
    def get_spd(self):
        raise NotImplementedError

    @abstractmethod
    def get_hp(self):
        raise NotImplementedError

    @abstractmethod
    def get_def(self):
        raise NotImplementedError
