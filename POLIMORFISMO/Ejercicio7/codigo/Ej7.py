#7. Se hace referencia a algunos animales mediante las siguientes clases: 
#a) Instanciar 1 Perro, 1 Gato y 1 Pájaro. 
#b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido característico. 
#c) Implementar un método moverse() que indique cómo se mueve cada animal (correr, saltar, volar, etc.). 
from multimethod import multimethod

class Perro:
    def __init__(self, nombre: str, edad: int, raza: str):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

class Gato:
    def __init__(self, nombre: str, color: str):
        self.nombre = nombre
        self.color = color

class Pajaro:
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo


perro = Perro("Firulais", 5, "Labrador")
gato = Gato("Michi", "Negro")
pajaro = Pajaro("Piolín", "Canario")


@multimethod
def hacerSonido(animal: Perro):
    print(f"{animal.nombre} dice: ¡Guau guau!")

@multimethod
def hacerSonido(animal: Gato):
    print(f"{animal.nombre} dice: ¡Miau!")

@multimethod
def hacerSonido(animal: Pajaro):
    print(f"{animal.nombre} dice: ¡Pío pío!")


@multimethod
def moverse(animal: Perro):
    print(f"{animal.nombre} corre en el parque.")

@multimethod
def moverse(animal: Gato):
    print(f"{animal.nombre} salta por los tejados.")

@multimethod
def moverse(animal: Pajaro):
    print(f"{animal.nombre} vuela por el cielo.")

print(" -----SONIDOS ----")
hacerSonido(perro)
hacerSonido(gato)
hacerSonido(pajaro)

print("\n----- MOVIMIENTOS -----")
moverse(perro)
moverse(gato)
moverse(pajaro)
