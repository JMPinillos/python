class Coordenada:

    def __init__(self, lon: float, lat: float):
        self.lon = lon
        self.lat = lat

    def __eq__(self, otro):
        return self.lon == otro.lon and self.lat == otro.lat


coordenadas1 = Coordenada(45, 27)
coordenadas2 = Coordenada(45, 27)

print(coordenadas1 == coordenadas2)
