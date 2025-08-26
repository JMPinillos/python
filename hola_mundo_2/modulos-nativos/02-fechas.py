# import time

# print(time.time())
from datetime import datetime

fecha = datetime.now()

print(fecha)

fechaStr = datetime.strptime("1984-03-27", "%Y-%m-%d")

print(fecha.strftime("%a %d de %b de %Y"))

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)
