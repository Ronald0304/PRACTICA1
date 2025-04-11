#7. Se hace referencia a algunos animales mediante las siguientes clases: 
#a) Instanciar 1 Perro, 1 Gato y 1 Pájaro. 
#b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido característico. 
#c) Implementar un método moverse() que indique cómo se mueve cada animal (correr, saltar, volar, etc.). 
class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def moverse(self):
        print(f"{self.nombre} corre.")


class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def moverse(self):
        print(f"{self.nombre} salta.")


class Pajaro:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Pío!")

    def moverse(self):
        print(f"{self.nombre} vuela.")


if __name__ == "__main__":
    perro = Perro("Firulais", 3, "Labrador")
    gato = Gato("Michi", "Blanco")
    pajaro = Pajaro("Piolín", "Canario")

    print("----- Sonidos -----")
    perro.hacer_sonido()
    gato.hacer_sonido()
    pajaro.hacer_sonido()

    print("\n----- Movimientos -----")
    perro.moverse()
    gato.moverse()
    pajaro.moverse()
