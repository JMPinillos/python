try:
    n1 = int(input("introduce tu primer numero: "))
except Exception as e:
    print("Ocurrio un error")
else:
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempre")
