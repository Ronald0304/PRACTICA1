//7. Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
//a) Crea un método para instalar una nueva aplicación
//b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan
//más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza un 1% cada 10 minutos de uso)
//c) Muestra el porcentaje de batería restante
//d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el mensaje de celular apagado
import java.util.ArrayList;

class Aplicacion {
    String nombre;
    int tamaño;

    public Aplicacion(String nombre, int tamaño) {
        this.nombre = nombre;
        this.tamaño = tamaño;
    }
}

class Celular {
    private int espacioTotal = 1024;
    private int maxApps = 20;
    private double bateria = 100.0;
    private ArrayList<Aplicacion> aplicaciones = new ArrayList<>();
    private int espacioOcupado = 0;

    public void instalarAplicacion(String nombre, int tamaño) {
        if (aplicaciones.size() >= maxApps) {
            System.out.println("No se pueden instalar más aplicaciones (límite alcanzado).");
            return;
        }

        if (espacioOcupado + tamaño > espacioTotal) {
            System.out.println("No hay suficiente espacio para instalar esta aplicación.");
            return;
        }

        aplicaciones.add(new Aplicacion(nombre, tamaño));
        espacioOcupado += tamaño;
        System.out.println("Aplicación '" + nombre + "' instalada correctamente.");
    }

    public void usarAplicacion(String nombre, int minutos) {
        if (bateria <= 0) {
            System.out.println("Celular apagado.");
            return;
        }

        Aplicacion app = null;
        for (Aplicacion a : aplicaciones) {
            if (a.nombre.equals(nombre)) {
                app = a;
                break;
            }
        }

        if (app == null) {
            System.out.println("La aplicación '" + nombre + "' no está instalada.");
            return;
        }

        int consumoPor10;
        if (app.tamaño > 250) {
            consumoPor10 = 5;
        } else if (app.tamaño > 100) {
            consumoPor10 = 2;
        } else {
            consumoPor10 = 1;
        }

        int bloques10Min = minutos / 10;
        double consumoTotal = bloques10Min * consumoPor10;

        bateria -= consumoTotal;
        if (bateria <= 0) {
            bateria = 0;
            System.out.println("La batería se ha agotado. Celular apagado.");
        } else {
            System.out.printf("Usaste la aplicación '%s' por %d minutos. Batería actual: %.2f%%%n",
                              nombre, minutos, bateria);
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
