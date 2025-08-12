class Coordenada:

    def __init__(self, lon: float, lat: float):
        self.lon = lon
        self.lat = lat

    def __eq__(self, otro):
        return self.lon == otro.lon and self.lat == otro.lat

    def __ne__(self, otro):
        return self.lon != otro.lon or self.lat != otro.lat

    def __lt__(self, otro):
        return self.lon + self.lat < otro.lon + otro.lat

    def __le__(self, otro):
        return self.lon + self.lat <= otro.lon + otro.lat


coordenadas1 = Coordenada(45, 27)
coordenadas2 = Coordenada(45, 27)

# print(coordenadas1 == coordenadas2)
# print(coordenadas1 != coordenadas2)


print(coordenadas1 < coordenadas2)
print(coordenadas1 <= coordenadas2)
