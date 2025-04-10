#1. Crea una clase Persona con nombre, edad y ciudad
#a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
#b) Crea tres personas y muestra su saludo
#c) Agrega un método para verificar si es mayor de edad

class Persona:
    def __init__(self,nombre,edad,ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludo(self):
        print("Hola soy ",self.nombre, " de ", self.ciudad)
    
    def medad(self):
        if self.edad >=18:
            print (self.nombre,"Es mayor de edad")
        else:
            print (self.nombre, "Es menor de edad")

Persona1 = Persona("Ronald", 17 , "La Paz")
Persona2 = Persona("Juan", 15 , "La Paz")
Persona3 = Persona("Jose", 19 , "La Paz")
Persona1.saludo()
Persona1.medad()
Persona2.saludo()
Persona3.saludo()
