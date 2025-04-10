class Coche:
    def __init__(self,marca,modelo,velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad +=10

    def frenar (self):
        self.velocidad -=5

auto1 = Coche("Toyota",2010,33)
auto2 = Coche("Zusuki",2012,19)

auto1.acelerar()
auto1.acelerar()
auto1.acelerar()
auto1.frenar()
auto2.acelerar()
auto2.acelerar()

print("La velocidad del",auto1.marca, " es" ,auto1.velocidad,"km/h")
print("La velocidad del",auto2.marca, " es" ,auto2.velocidad,"km/h")
