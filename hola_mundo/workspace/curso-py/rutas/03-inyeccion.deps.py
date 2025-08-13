from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependecias = {
    "db": "base de datos",
    "api": "api",
    "graphql": "graphql"
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependecias)
    except:
        print("el paquete no tiene función init")


list(map(load, paths))
