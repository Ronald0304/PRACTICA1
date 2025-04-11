//9. Para los bloques del juego Minecraft se usará los siguientes objetos: 
//a) Crear e instanciar al menos 2 bloques de cada tipo 
//b) Sobrescribe accion() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque. 
//c) Sobrecarga colocar() para permitir colocar un bloque en diferentes orientaciones (por ejemplo, en el suelo o en la pared). 
//d) Sobrescribe romper() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque y que puede suceder al romperlos.
class BloqueCofre {
    private int capacidad;
    private int resistencia;
    private String tipo;

    public BloqueCofre(int capacidad, int resistencia, String tipo) {
        this.capacidad = capacidad;
        this.resistencia = resistencia;
        this.tipo = tipo;
    }

    public void accion() {
        System.out.println("Abriste el cofre de tipo " + tipo + ". Puedes guardar objetos.");
    }

    public void colocar(String orientacion) {
        System.out.println("Colocaste el cofre orientado hacia " + orientacion + ".");
    }

    public void romper() {
        System.out.println("El cofre se ha roto. Los objetos caen al suelo.");
    }
}

class BloqueTnt {
    private String tipo;
    private int daño;

    public BloqueTnt(String tipo, int daño) {
        this.tipo = tipo;
        this.daño = daño;
    }

    public void accion() {
        System.out.println("Activaste la TNT de tipo " + tipo + ". ¡Cuidado con la explosión!");
    }

    public void colocar(String orientacion) {
        System.out.println("Colocaste la TNT en la orientación: " + orientacion + ".");
    }

    public void romper() {
        System.out.println("¡La TNT explotó al romperse!");
    }
}

class BloqueHorno {
    private String color;
    private int capacidadComida;

    public BloqueHorno(String color, int capacidadComida) {
        this.color = color;
        this.capacidadComida = capacidadComida;
    }

    public void accion() {
        System.out.println("Encendiste el horno " + color + ". Puedes cocinar hasta " + capacidadComida + " alimentos.");
    }

    public void colocar(String orientacion) {
        System.out.println("Colocaste el horno en la orientación: " + orientacion + ".");
    }

    public void romper() {
        System.out.println("El horno se rompió. Se pierde la comida cocinándose.");
    }
}

public class Main {
    public static void main(String[] args) {
        BloqueCofre cofre1 = new BloqueCofre(30, 50, "Roble");
        BloqueCofre cofre2 = new BloqueCofre(40, 60, "Abeto");

        BloqueTnt tnt1 = new BloqueTnt("Clásica", 100);
        BloqueTnt tnt2 = new BloqueTnt("Mega", 200);

        BloqueHorno horno1 = new BloqueHorno("Negro", 5);
        BloqueHorno horno2 = new BloqueHorno("Gris", 8);

        System.out.println("----- ACCIONES -----");
        cofre1.accion();
        cofre2.accion();
        tnt1.accion();
        tnt2.accion();
        horno1.accion();
        horno2.accion();

        System.out.println("\n----- COLOCAR -----");
        cofre1.colocar("norte");
        tnt1.colocar("suelo");
        horno1.colocar("pared");

        System.out.println("\n----- ROMPER -----");
        cofre2.romper();
        tnt2.romper();
        horno2.romper();
    }
}
