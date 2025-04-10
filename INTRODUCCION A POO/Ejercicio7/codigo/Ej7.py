#7. Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
#a) Crea un método para instalar una nueva aplicación
#b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan
#más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza un 1% cada 10 minutos de uso)
#c) Muestra el porcentaje de batería restante
#d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el mensaje de celular apagado
class Celular:
    def __init__(self):
        self.espacio_total = 1024  
        self.max_apps = 20
        self.bateria = 100.0  
        self.aplicaciones = []  
        self.espacio_ocupado = 0

    def instalar_aplicacion(self, nombre, tamaño):
        if len(self.aplicaciones) >= self.max_apps:
            print("No se pueden instalar más aplicaciones (límite alcanzado).")
            return

        if self.espacio_ocupado + tamaño > self.espacio_total:
            print("No hay suficiente espacio para instalar esta aplicación.")
            return

        self.aplicaciones.append({'nombre': nombre, 'tamaño': tamaño})
        self.espacio_ocupado += tamaño
        print(f"Aplicación '{nombre}' instalada correctamente.")

    def usar_aplicacion(self, nombre, minutos):
        if self.bateria <= 0:
            print("Celular apagado.")
            return

        app = next((app for app in self.aplicaciones if app['nombre'] == nombre), None)
        if not app:
            print(f"La aplicación '{nombre}' no está instalada.")
            return

        tamaño = app['tamaño']
        if tamaño > 250:
            consumo_por_10 = 5
        elif tamaño > 100:
            consumo_por_10 = 2
        else:
            consumo_por_10 = 1

        bloques_10_min = minutos // 10
        consumo_total = bloques_10_min * consumo_por_10

        self.bateria -= consumo_total
        if self.bateria <= 0:
            self.bateria = 0
            print("La batería se ha agotado. Celular apagado.")
        else:
            print(f"Usaste la aplicación '{nombre}' por {minutos} minutos. Batería actual: {self.bateria:.2f}%")

    def mostrar_bateria(self):
        print(f"Batería restante: {self.bateria:.2f}%")
cel = Celular()

cel.instalar_aplicacion("WhatsApp", 150)
cel.instalar_aplicacion("Instagram", 300)
cel.instalar_aplicacion("Notas", 50)

cel.mostrar_bateria()

cel.usar_aplicacion("Instagram", 30)  
cel.usar_aplicacion("Notas", 20)      
cel.usar_aplicacion("WhatsApp", 40)   

cel.mostrar_bateria()
