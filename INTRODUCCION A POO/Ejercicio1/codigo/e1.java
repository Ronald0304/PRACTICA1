//1. Crea una clase Persona con nombre, edad y ciudad
//a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
//b) Crea tres personas y muestra su saludo
//c) Agrega un método para verificar si es mayor de edad

public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public void saludo() {
        System.out.println("Hola soy " + nombre + " de " + ciudad);
    }

    public void medad() {
        if (edad >= 18) {
            System.out.println(nombre + " es mayor de edad");
        } else {
            System.out.println(nombre + " es menor de edad");
        }
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Ronald", 17, "La Paz");
        Persona persona2 = new Persona("Juan", 15, "La Paz");
        Persona persona3 = new Persona("Jose", 19, "La Paz");

        persona1.saludo();
        persona1.medad();
        persona2.saludo();
        persona3.saludo();
    }
}
