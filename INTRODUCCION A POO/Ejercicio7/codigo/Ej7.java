//7. Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
//a) Crea un método para instalar una nueva aplicación
//b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan
//más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza un 1% cada 10 minutos de uso)
//c) Muestra el porcentaje de batería restante
//d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el mensaje de celular apagado
import java.util.ArrayList;
import java.util.HashMap;

public class Celular {
    int espacio_total = 1024;
    int max_apps = 20;
    double bateria = 100.0;
    ArrayList<HashMap<String, Object>> aplicaciones = new ArrayList<>();
    int espacio_ocupado = 0;

    public void instalar_aplicacion(String nombre, int tamano) {
        if (aplicaciones.size() >= max_apps) {
            System.out.println("No se pueden instalar más aplicaciones (límite alcanzado).");
            return;
        }

        if (espacio_ocupado + tamano > espacio_total) {
            System.out.println("No hay suficiente espacio para instalar esta aplicación.");
            return;
        }

        HashMap<String, Object> app = new HashMap<>();
        app.put("nombre", nombre);
        app.put("tamaño", tamano);
        aplicaciones.add(app);
        espacio_ocupado += tamano;

        System.out.println("Aplicación '" + nombre + "' instalada correctamente.");
    }

    public void usar_aplicacion(String nombre, int minutos) {
        if (bateria <= 0) {
            System.out.println("Celular apagado.");
            return;
        }

        HashMap<String, Object> app = null;
        for (HashMap<String, Object> a : aplicaciones) {
            if (a.get("nombre").equals(nombre)) {
                app = a;
                break;
            }
        }

        if (app == null) {
            System.out.println("La aplicación '" + nombre + "' no está instalada.");
            return;
        }

        int tamano = (int) app.get("tamano");
        int consumo_por_10;
        if (tamano > 250) {
            consumo_por_10 = 5;
        } else if (tamano > 100) {
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

    public void mostrar_bateria() {
        System.out.printf("Batería restante: %.2f%%%n", bateria);
    }

    public static void main(String[] args) {
        Celular cel = new Celular();

        cel.instalar_aplicacion("WhatsApp", 150);
        cel.instalar_aplicacion("Instagram", 300);
        cel.instalar_aplicacion("Notas", 50);

        cel.mostrar_bateria();

        cel.usar_aplicacion("Instagram", 30); 
        cel.usar_aplicacion("Notas", 20);    
        cel.usar_aplicacion("WhatsApp", 40);   

        cel.mostrar_bateria();
    }
}

