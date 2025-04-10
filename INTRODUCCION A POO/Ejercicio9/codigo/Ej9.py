#9. Realiza la abstracción de una Computadora
#a) Muestra los componentes principales de la computadora
#b) Muestra el estado de la computadora (encendido o apagado)
#c) Crea una instancia y simula encender y apagar la computadora.
class Computadora:
    def __init__(self):
        self.estado = "Apagada"
        self.componentes = []

    def agregar_componente(self, nombre, tipo):
        componente = {"nombre": nombre, "tipo": tipo}
        self.componentes.append(componente)

    def encender(self):
        if self.estado == "Apagada":
            self.estado = "Encendida"
            print("La computadora está encendida.")
        else:
            print("La computadora ya está encendida.")

    def apagar(self):
        if self.estado == "Encendida":
            self.estado = "Apagada"
            print("La computadora está apagada.")
        else:
            print("La computadora ya está apagada.")

    def mostrar_componentes(self):
        print("Componentes de la computadora:")
        for componente in self.componentes:
            print(f"{componente['tipo']}: {componente['nombre']}")

mi_computadora = Computadora()

mi_computadora.agregar_componente("Intel i7", "CPU")
mi_computadora.agregar_componente("16GB DDR4", "RAM")
mi_computadora.agregar_componente("1TB SSD", "Disco Duro")
mi_computadora.agregar_componente("NVIDIA GTX 1660", "Tarjeta Gráfica")
mi_computadora.agregar_componente("lcd", "Pantalla")

mi_computadora.mostrar_componentes()

mi_computadora.encender()  
mi_computadora.apagar()    
