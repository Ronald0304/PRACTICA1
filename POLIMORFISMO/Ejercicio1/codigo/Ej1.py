from multimethod import multimethod

class Videojuego:
    def __init__(self, nombre="Desconocido", plataforma="Desconocida", cantidadaJugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadaJugadores = cantidadaJugadores

    @classmethod
    def desdeNombre(cls, nombre):
        return cls(nombre)

    @classmethod
    def desdeNombreYPlataforma(cls, nombre, plataforma):
        return cls(nombre, plataforma)

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Cantidad de Jugadores: {self.cantidadaJugadores}")

    @multimethod
    def agregarJugadores(self):
        self.cantidadaJugadores += 1

    @multimethod
    def agregarJugadores(self, cantidad: int):
        self.cantidadaJugadores += cantidad

v1 = Videojuego.desdeNombreYPlataforma("FIFA 24", "PlayStation 5")
v2 = Videojuego.desdeNombre("Minecraft")

v1.agregarJugadores()
v2.agregarJugadores(3)

v1.mostrar()
print()
v2.mostrar()
