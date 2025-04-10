from multimethod import multimethod

class Cocinero:
    def __init__(self, nombre: str, sueldoMes: int, horasExtra: int, sueldoHora: float):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__horasExtra = horasExtra
        self.__sueldoHora = sueldoHora

    @multimethod
    def SueldoTotal(self):
        total = self.__sueldoMes + (self.__horasExtra * self.__sueldoHora)
        print(f"Cocinero {self.__nombre} - Sueldo Total: {total}")

    @multimethod
    def SueldoTotal(self, sueldoFiltro: int):
        if self.__sueldoMes == sueldoFiltro:
            print(f"Cocinero {self.__nombre} - SueldoMes igual a {sueldoFiltro}")


class Mesero:
    def __init__(self, nombre: str, sueldoMes: int, horasExtra: int, sueldoHora: float, propina: float):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__horasExtra = horasExtra
        self.__sueldoHora = sueldoHora
        self.__propina = propina

    @multimethod
    def SueldoTotal(self):
        total = self.__sueldoMes + (self.__horasExtra * self.__sueldoHora) + self.__propina
        print(f"Mesero {self.__nombre} - Sueldo Total: {total}")

    @multimethod
    def SueldoTotal(self, sueldoFiltro: int):
        if self.__sueldoMes == sueldoFiltro:
            print(f"Mesero {self.__nombre} - SueldoMes igual a {sueldoFiltro}")


class Administrativo:
    def __init__(self, nombre: str, sueldoMes: float, cargo: str):
        self.__nombre = nombre
        self.__sueldoMes = sueldoMes
        self.__cargo = cargo

    @multimethod
    def SueldoTotal(self):
        print(f"Administrativo {self.__nombre} - Sueldo Total: {self.__sueldoMes}")

    @multimethod
    def SueldoTotal(self, sueldoFiltro: int):
        if self.__sueldoMes == sueldoFiltro:
            print(f"Administrativo {self.__nombre} - SueldoMes igual a {sueldoFiltro}")

c1 = Cocinero("Carlos", 3000, 10, 50)
m1 = Mesero("Ana", 2800, 8, 40, 200)
m2 = Mesero("Luis", 2900, 5, 45, 150)
a1 = Administrativo("Sofía", 3200, "Contadora")
a2 = Administrativo("Jorge", 3200, "RRHH")

print("------ Sueldos Totales ------")
c1.SueldoTotal()
m1.SueldoTotal()
m2.SueldoTotal()
a1.SueldoTotal()
a2.SueldoTotal()

print("\n---- Empleados con sueldo del Mes = 3200 ---")
c1.SueldoTotal(3200)
m1.SueldoTotal(3200)
m2.SueldoTotal(3200)
a1.SueldoTotal(3200)
a2.SueldoTotal(3200)
