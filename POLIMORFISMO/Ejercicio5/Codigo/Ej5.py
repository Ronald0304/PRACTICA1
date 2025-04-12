#5. Se hace referencia a algunos de los diferentes ambientes de la Universidad mediante las siguientes clases:
#a) Instanciar 2 objetos Oficina, 2 Aulas y 1 Laboratorio 
#b) Crear un método mostrar() para mostrar los datos de cada objeto 
#c) Sobrecargar el método cantidadMuebles(), para conocer el número total de muebles dentro de cada ambiente
from multimethod import multimethod

class Oficina:
    def __init__(self, nroSillas: int, nroEscritorios: int, nroEstanterias: int):
        self.__nroSillas = nroSillas
        self.__nroEscritorios = nroEscritorios
        self.__nroEstanterias = nroEstanterias

    def mostrar(self):
        print(f"Oficina - Sillas: {self.__nroSillas}, Escritorios: {self.__nroEscritorios}, Estanterías: {self.__nroEstanterias}")

    @multimethod
    def cantidadMuebles(self):
        total = self.__nroSillas + self.__nroEscritorios + self.__nroEstanterias
        print(f"Oficina - Total de muebles: {total}")
        return total

    @multimethod
    def cantidadMuebles(self, tipo: str):
        if tipo == "sillas":
            print(f"Oficina - Total de sillas: {self.__nroSillas}")
            return self.__nroSillas
        elif tipo == "escritorios":
            print(f"Oficina - Total de escritorios: {self.__nroEscritorios}")
            return self.__nroEscritorios
        elif tipo == "estanterias":
            print(f"Oficina - Total de estanterías: {self.__nroEstanterias}")
            return self.__nroEstanterias
        else:
            print("Tipo de mueble no reconocido.")
            return 0

class Aula:
    def __init__(self, nombre: str, capacidad: int, nroPupitres: int):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__nroPupitres = nroPupitres

    def mostrar(self):
        print(f"Aula - Nombre: {self.__nombre}, Capacidad: {self.__capacidad}, Pupitres: {self.__nroPupitres}")

    @multimethod
    def cantidadMuebles(self):
        total = self.__nroPupitres
        print(f"Aula - {self.__nombre} - Total de muebles (pupitres): {total}")
        return total

    @multimethod
    def cantidadMuebles(self, tipo: str):
        if tipo == "pupitres":
            print(f"Aula - {self.__nombre} - Total de pupitres: {self.__nroPupitres}")
            return self.__nroPupitres
        else:
            print("Tipo de mueble no reconocido.")
            return 0

class Laboratorio:
    def __init__(self, nombre: str, capacidad: int, nroMesas: int, nroSillas: int):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__nroMesas = nroMesas
        self.__nroSillas = nroSillas

    def mostrar(self):
        print(f"Laboratorio - Nombre: {self.__nombre}, Capacidad: {self.__capacidad}, Mesas: {self.__nroMesas}, Sillas: {self.__nroSillas}")

    @multimethod
    def cantidadMuebles(self):
        total = self.__nroMesas + self.__nroSillas
        print(f"Laboratorio - {self.__nombre} - Total de muebles: {total}")
        return total

    @multimethod
    def cantidadMuebles(self, tipo: str):
        if tipo == "mesas":
            print(f"Laboratorio - {self.__nombre} - Total de mesas: {self.__nroMesas}")
            return self.__nroMesas
        elif tipo == "sillas":
            print(f"Laboratorio - {self.__nombre} - Total de sillas: {self.__nroSillas}")
            return self.__nroSillas
        else:
            print("Tipo de mueble no reconocido.")
            return 0

if __name__ == "__main__":
    o1 = Oficina(4, 2, 1)
    o2 = Oficina(6, 3, 2)

    a1 = Aula("Aula A", 30, 30)
    a2 = Aula("Aula B", 25, 25)

    l1 = Laboratorio("Lab Física", 20, 10, 20)

    print("------- Mostrar datos --------")
    o1.mostrar()
    o2.mostrar()
    a1.mostrar()
    a2.mostrar()
    l1.mostrar()

    print("\n----- Cantidad de muebles -----")
    o1.cantidadMuebles()
    o2.cantidadMuebles()
    a1.cantidadMuebles()
    a2.cantidadMuebles()
    l1.cantidadMuebles()

    print("\n----- Cantidad de muebles por tipo -----")
    o1.cantidadMuebles("sillas")
    o2.cantidadMuebles("escritorios")
    a1.cantidadMuebles("pupitres")
    l1.cantidadMuebles("mesas")
    l1.cantidadMuebles("sillas")
