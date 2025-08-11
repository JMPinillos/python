from abc import ABC, abstractmethod


class Model(ABC):

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id: int):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("Guardando usuario")


usuario = Usuario()
Usuario.buscar_por_id(124)
usuario.guardar()
