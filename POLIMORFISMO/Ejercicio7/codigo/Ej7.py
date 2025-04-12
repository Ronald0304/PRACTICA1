#7. Se hace referencia a algunos animales mediante las siguientes clases: 
#a) Instanciar 1 Perro, 1 Gato y 1 Pájaro. 
#b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido característico. 
#c) Implementar un método moverse() que indique cómo se mueve cada animal (correr, saltar, volar, etc.). 
from multimethod import multimethod

class Perro:
    def __init__(self, nombre, edad, raza):
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    @multimethod
    def hacerSonido(self):
        print(f"{self._nombre} dice: ¡Guau!")

    @multimethod
    def hacerSonido(self, sonido: str):
        print(f"{self._nombre} dice: {sonido}")

    def moverse(self):
        print(f"{self._nombre} corre.")


class Gato:
    def __init__(self, nombre, color):
        self._nombre = nombre
        self._color = color

    @multimethod
    def hacerSonido(self):
        print(f"{self._nombre} dice: ¡Miau!")

    @multimethod
    def hacerSonido(self, sonido: str):
        print(f"{self._nombre} dice: {sonido}")

    def moverse(self):
        print(f"{self._nombre} salta.")


class Pajaro:
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo

    @multimethod
    def hacerSonido(self):
        print(f"{self._nombre} dice: ¡Pío!")

    @multimethod
    def hacerSonido(self, sonido: str):
        print(f"{self._nombre} dice: {sonido}")

    def moverse(self):
        print(f"{self._nombre} vuela.")


if __name__ == "__main__":
    perro = Perro("Firulais", 3, "Labrador")
    gato = Gato("Michi", "Blanco")
    pajaro = Pajaro("Piolín", "Canario")

    print("----- Sonidos -----")
    perro.hacerSonido()  
    perro.hacerSonido("¡Guau Guau!")  
    gato.hacerSonido() 
    gato.hacerSonido("¡Miau Miau!")  
    pajaro.hacerSonido()  
    pajaro.hacerSonido("¡Pío Pío!")  

    print("\n----- Movimientos -----")
    perro.moverse()
    gato.moverse()
    pajaro.moverse()
