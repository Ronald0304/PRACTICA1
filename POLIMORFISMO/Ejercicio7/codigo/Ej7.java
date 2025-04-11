//7. Se hace referencia a algunos animales mediante las siguientes clases: 
//a) Instanciar 1 Perro, 1 Gato y 1 Pájaro. 
//b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido característico. 
//c) Implementar un método moverse() que indique cómo se mueve cada animal (correr, saltar, volar, etc.).
class Perro {
    private String nombre;
    private int edad;
    private String raza;

    public Perro(String nombre, int edad, String raza) {
        this.nombre = nombre;
        this.edad = edad;
        this.raza = raza;
    }

    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Guau!");
    }

    public void moverse() {
        System.out.println(nombre + " corre.");
    }
}

class Gato {
    private String nombre;
    private String color;

    public Gato(String nombre, String color) {
        this.nombre = nombre;
        this.color = color;
    }

    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Miau!");
    }

    public void moverse() {
        System.out.println(nombre + " salta.");
    }
}

class Pajaro {
    private String nombre;
    private String tipo;

    public Pajaro(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
    }

    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Pío!");
    }

    public void moverse() {
        System.out.println(nombre + " vuela.");
    }
}

public class Main {
    public static void main(String[] args) {
        Perro perro = new Perro("Firulais", 3, "Labrador");
        Gato gato = new Gato("Michi", "Blanco");
        Pajaro pajaro = new Pajaro("Piolín", "Canario");

        System.out.println("----- Sonidos -----");
        perro.hacerSonido();
        gato.hacerSonido();
        pajaro.hacerSonido();

        System.out.println("\n----- Movimientos -----");
        perro.moverse();
        gato.moverse();
        pajaro.moverse();
    }
}

