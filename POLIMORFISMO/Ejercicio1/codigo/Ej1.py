#1.Sea la clase Videojuego:
#a)Instanciar al menos 2 videojuegos
#b)Sobrecargar el constructor 2 veces
#c)Implementar un método mostrar()
#d)Sobrecargar el método agregarJugadores() donde en el primero se agregue solo 1 jugador y en otro se ingrese una cantidad de jugadores a aumentar.
from multimethod import multimethod

class Videojuego:
    def __init__(self, nombre="Desconocido", plataforma="Desconocida", cantidadaJugadores=0):
        self.__nombre = nombre
        self.__plataforma = plataforma
        self.__cantidadaJugadores = cantidadaJugadores

    @classmethod
    def desdeNombre(cls, nombre):
        return cls(nombre)

    @classmethod
    def desdeNombreYPlataforma(cls, nombre, plataforma):
        return cls(nombre, plataforma)

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Plataforma: {self.__plataforma}")
        print(f"Cantidad de Jugadores: {self.__cantidadaJugadores}")

    @multimethod
    def agregarJugadores(self):
        self.__cantidadaJugadores += 1

    @multimethod
    def agregarJugadores(self, cantidad: int):
        self.__cantidadaJugadores += cantidad

v1 = Videojuego.desdeNombreYPlataforma("FIFA 24", "PlayStation 5")
v2 = Videojuego.desdeNombre("Minecraft")

v1.agregarJugadores()
v2.agregarJugadores(3)

v1.mostrar()
print()
v2.mostrar()
