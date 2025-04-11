//7. Se hace referencia a algunos animales mediante las siguientes clases: 
//a) Instanciar 1 Perro, 1 Gato y 1 Pájaro. 
//b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido característico. 
//c) Implementar un método moverse() que indique cómo se mueve cada animal (correr, saltar, volar, etc.).
public class Perro {
    private String nombre;
    private int edad;
    private String raza;

    public Perro(String nombre, int edad, String raza) {
        this.nombre = nombre;
        this.edad = edad;
        this.raza = raza;
    }

    public String getNombre() {
        return nombre;
    }
}

public class Gato {
    private String nombre;
    private String color;

    public Gato(String nombre, String color) {
        this.nombre = nombre;
        this.color = color;
    }

    public String getNombre() {
        return nombre;
    }
}

public class Pajaro {
    private String nombre;
    private String tipo;

    public Pajaro(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
    }

    public String getNombre() {
        return nombre;
    }
}
public class AnimalesTest {

    public static void hacerSonido(Perro p) {
        System.out.println(p.getNombre() + " dice: ¡Guau guau!");
    }

    public static void hacerSonido(Gato g) {
        System.out.println(g.getNombre() + " dice: ¡Miau!");
    }

    public static void hacerSonido(Pajaro pa) {
        System.out.println(pa.getNombre() + " dice: ¡Pío pío!");
    }

    public static void moverse(Perro p) {
        System.out.println(p.getNombre() + " corre en el parque.");
    }

    public static void moverse(Gato g) {
        System.out.println(g.getNombre() + " salta por los tejados.");
    }

    public static void moverse(Pajaro pa) {
        System.out.println(pa.getNombre() + " vuela por el cielo.");
    }

    public static void main(String[] args) {
        Perro perro = new Perro("Firulais", 5, "Labrador");
        Gato gato = new Gato("Michi", "Negro");
        Pajaro pajaro = new Pajaro("Piolín", "Canario");

        System.out.println("== SONIDOS ==");
        hacerSonido(perro);
        hacerSonido(gato);
        hacerSonido(pajaro);

        System.out.println("\n== MOVIMIENTOS ==");
        moverse(perro);
        moverse(gato);
        moverse(pajaro);
    }
}
