# PARTE 1
# from abc import ABC, abstractmethod


# class Model(ABC):

#     @abstractmethod
#     def guardar(self):
#         pass


# class Usuario(Model):
#     def guardar(self):
#         print("Usuario guardado")


# class Sesion(Model):
#     def guardar(self):
#         print("Guardando sesión")


# def guardar(entidades):
#     for entidad in entidades:
#         entidad.guardar()


# usuario = Usuario()
# # guardar(usuario)
# # print("------------")

# sesion = Sesion()
# # guardar(sesion)
# # print("------------")

# guardar([sesion, usuario])

# PARTE 2

class Usuario():
    def guardar(self):
        print("Usuario guardado")


class Sesion():
    def guardar(self):
        print("Guardando sesión")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])
