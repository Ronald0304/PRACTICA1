#9. Para los bloques del juego Minecraft se usará los siguientes objetos: 
#a) Crear e instanciar al menos 2 bloques de cada tipo 
#b) Sobrescribe accion() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque. 
#c) Sobrecarga colocar() para permitir colocar un bloque en diferentes orientaciones (por ejemplo, en el suelo o en la pared). 
#d) Sobrescribe romper() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque y que puede suceder al romperlos.
from multimethod import multimethod

class BloqueCofre:
    def __init__(self, capacidad, resistencia, tipo):
        self._capacidad = capacidad
        self._resistencia = resistencia
        self._tipo = tipo

    def accion(self):
        print(f"Abriste el cofre de tipo {self._tipo}. Puedes guardar objetos.")

    @multimethod
    def colocar(self, orientacion: str):
        print(f"Colocaste el cofre orientado hacia {orientacion}.")

    @multimethod
    def colocar(self, orientacion: str, altura: int):
        print(f"Colocaste el cofre orientado hacia {orientacion} a una altura de {altura}.")

    def romper(self):
        print("El cofre se ha roto. Los objetos caen al suelo.")


class BloqueTnt:
    def __init__(self, tipo, daño):
        self._tipo = tipo
        self._daño = daño

    def accion(self):
        print(f"Activaste la TNT de tipo {self._tipo}. ¡Cuidado con la explosión!")

    @multimethod
    def colocar(self, orientacion: str):
        print(f"Colocaste la TNT en la orientación: {orientacion}.")

    @multimethod
    def colocar(self, orientacion: str, altura: int):
        print(f"Colocaste la TNT en la orientación: {orientacion} a una altura de {altura}.")

    def romper(self):
        print("¡La TNT explotó al romperse!")


class BloqueHorno:
    def __init__(self, color, capacidad_comida):
        self._color = color
        self._capacidad_comida = capacidad_comida

    def accion(self):
        print(f"Encendiste el horno {self._color}. Puedes cocinar hasta {self._capacidad_comida} alimentos.")

    @multimethod
    def colocar(self, orientacion: str):
        print(f"Colocaste el horno en la orientación: {orientacion}.")

    @multimethod
    def colocar(self, orientacion: str, altura: int):
        print(f"Colocaste el horno en la orientación: {orientacion} a una altura de {altura}.")

    def romper(self):
        print("El horno se rompió. Se pierde la comida cocinándose.")


if __name__ == "__main__":
    cofre1 = BloqueCofre(30, 50, "Roble")
    cofre2 = BloqueCofre(40, 60, "Abeto")

    tnt1 = BloqueTnt("Clásica", 100)
    tnt2 = BloqueTnt("Mega", 200)

    horno1 = BloqueHorno("Negro", 5)
    horno2 = BloqueHorno("Gris", 8)

    print("----- ACCIONES -----")
    cofre1.accion()
    cofre2.accion()
    tnt1.accion()
    tnt2.accion()
    horno1.accion()
    horno2.accion()

    print("\n----- COLOCAR -----")
    cofre1.colocar("norte")
    cofre1.colocar("norte", 5)
    tnt1.colocar("suelo")
    tnt1.colocar("suelo", 3)
    horno1.colocar("pared")
    horno1.colocar("pared", 2)

    print("\n----- ROMPER -----")
    cofre2.romper()
    tnt2.romper()
    horno2.romper()

