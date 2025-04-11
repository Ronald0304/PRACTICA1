#9. Para los bloques del juego Minecraft se usará los siguientes objetos: 
#a) Crear e instanciar al menos 2 bloques de cada tipo 
#b) Sobrescribe accion() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque. 
#c) Sobrecarga colocar() para permitir colocar un bloque en diferentes orientaciones (por ejemplo, en el suelo o en la pared). 
#d) Sobrescribe romper() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque y que puede suceder al romperlos.
from multimethod import multimethod

class BloqueCofre:
    def __init__(self, capacidad: int, resistencia: int, tipo: str):
        self.__capacidad = capacidad
        self.__resistencia = resistencia
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

class BloqueTnt:
    def __init__(self, tipo: str, daño: int):
        self.__tipo = tipo
        self.__daño = daño

    def get_tipo(self):
        return self.__tipo

class BloqueHorno:
    def __init__(self, color: str, capacidadComida: int):
        self.__color = color
        self.__capacidadComida = capacidadComida

    def get_color(self):
        return self.__color

cofre1 = BloqueCofre(27, 10, "Cofre grande")
cofre2 = BloqueCofre(15, 7, "Cofre pequeño")

tnt1 = BloqueTnt("TNT normal", 100)
tnt2 = BloqueTnt("TNT mega", 300)

horno1 = BloqueHorno("Gris", 3)
horno2 = BloqueHorno("Negro", 6)

@multimethod
def accion(bloque: BloqueCofre):
    print(f"Abriste un {bloque.get_tipo()} para guardar objetos.")

@multimethod
def accion(bloque: BloqueTnt):
    print(f"Encendiste {bloque.get_tipo()}... ¡BOOM!")

@multimethod
def accion(bloque: BloqueHorno):
    print(f"Usaste un horno {bloque.get_color()} para cocinar comida.")

@multimethod
def colocar(bloque: BloqueCofre):
    print(f"{bloque.get_tipo()} colocado en el suelo.")

@multimethod
def colocar(bloque: BloqueTnt):
    print(f"{bloque.get_tipo()} colocado en la pared con cuidado.")

@multimethod
def colocar(bloque: BloqueHorno):
    print(f"Horno {bloque.get_color()} colocado junto a una mesa de trabajo.")

@multimethod
def romper(bloque: BloqueCofre):
    print(f"El {bloque.get_tipo()} se rompió y soltó sus objetos.")

@multimethod
def romper(bloque: BloqueTnt):
    print(f"¡Cuidado! Romper {bloque.get_tipo()} lo hace explotar.")

@multimethod
def romper(bloque: BloqueHorno):
    print(f"Horno {bloque.get_color()} roto. Ya no puedes cocinar con él.")

print("----- ACCIONES -----")
accion(cofre1)
accion(tnt1)
accion(horno1)

print("\n----- COLOCAR -----")
colocar(cofre2)
colocar(tnt2)
colocar(horno2)

print("\n----- ROMPER -----")
romper(cofre1)
romper(tnt2)
romper(horno1)
