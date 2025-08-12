

if __name__ != "__main__":
    from usuarios.gestion.crud import guardar

    print(__name__)

    def pagar_impuestos():
        print("Pagando impuestos")
        guardar()
