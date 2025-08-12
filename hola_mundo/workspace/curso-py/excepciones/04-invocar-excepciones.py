def division(n):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por 0", f"{n}")
    else:
        return 5/n


try:
    print(division(0))
except ZeroDivisionError as e:
    print(e)
