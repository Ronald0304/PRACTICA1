//7. Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
//a) Crea un método para instalar una nueva aplicación
//b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan
//más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza un 1% cada 10 minutos de uso)
//c) Muestra el porcentaje de batería restante
//d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el mensaje de celular apagado
import java.util.ArrayList;

public class Celular {
    public int espacio_total = 1024;
    public int max_apps = 20;
    public double bateria = 100.0;
    public ArrayList<String> nombresAplicaciones = new ArrayList<>();
    public ArrayList<Integer> tamaniosAplicaciones = new ArrayList<>();
    public int espacio_ocupado = 0;

    public void instalarAplicacion(String nombre, int tamaño) {
        if (nombresAplicaciones.size() >= max_apps) {
            System.out.println("No se pueden instalar más aplicaciones (límite alcanzado).");
            return;
        }

        if (espacio_ocupado + tamaño > espacio_total) {
            System.out.println("No hay suficiente espacio para instalar esta aplicación.");
            return;
        }

        nombresAplicaciones.add(nombre);
        tamaniosAplicaciones.add(tamaño);
        espacio_ocupado += tamaño;
        System.out.println("Aplicación '" + nombre + "' instalada correctamente.");
    }

    public void usarAplicacion(String nombre, int minutos) {
        if (bateria <= 0) {
            System.out.println("Celular apagado.");
            return;
        }

        int index = nombresAplicaciones.indexOf(nombre);
        if (index == -1) {
            System.out.println("La aplicación '" + nombre + "' no está instalada.");
            return;
        }

        int tamaño = tamaniosAplicaciones.get(index);
        int consumo_por_10;
        if (tamaño > 250) {
            consumo_por_10 = 5;
        } else if (tamaño > 100) {
            consumo_por_10 = 2;
        } else {
            consumo_por_10 = 1;
        }

        int bloques_10_min = minutos / 10;
        double consumo_total = bloques_10_min * consumo_por_10;

        bateria -= consumo_total;
        if (bateria <= 0) {
            bateria = 0;
            System.out.println("La batería se ha agotado. Celular apagado.");
        } else {
            System.out.printf("Usaste la aplicación '%s' por %d minutos. Batería actual: %.2f%%%n", nombre, minutos, bateria);
        }
    }

    public void mostrarBateria() {
        System.out.printf("Batería restante: %.2f%%%n", bateria);
    }

    public static void main(String[] args) {
        Celular cel = new Celular();

        cel.instalarAplicacion("WhatsApp", 150);
        cel.instalarAplicacion("Instagram", 300);
        cel.instalarAplicacion("Notas", 50);

        cel.mostrarBateria();

        cel.usarAplicacion("Instagram", 30);
        cel.usarAplicacion("Notas", 20);
        cel.usarAplicacion("WhatsApp", 40);

        cel.mostrarBateria();
    }
}


