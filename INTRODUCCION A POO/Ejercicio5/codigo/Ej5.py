#5. Crea una clase Estudiante con nombre, nota_1, nota_2
#a) Agrega un método para calcular el promedio
#b) Agrega un método para verificar si aprobó (promedio >=6)
#c) Crea tres estudiantes, muestra sus promedios y si aprobaron
class Estudiante:
    def __init__(self,nombre,nota_1,nota_2):
        self.nombre = nombre
        self.nota1 = nota_1
        self.nota2 = nota_2

    def promedio(self):
        self.media = (self.nota1 + self.nota2)/2
        return self.media
    
    def vaprob (self):
        if self.media>= 6:
            print (self.nombre, " Aprobo con ",self.media)
        else:
            print (self.nombre, " Reprobo con ",self.media)

e1 = Estudiante("Jose",1,2)
e2 = Estudiante("Juan",5,5)
e3 = Estudiante("Jhoel",9,7)

print("El promedio de ",e1.nombre," es de ",e1.promedio())
print("El promedio de ",e2.nombre," es de ",e2.promedio())
print("El promedio de ",e3.nombre," es de ",e3.promedio())
e1.vaprob()
e2.vaprob()
e3.vaprob()
