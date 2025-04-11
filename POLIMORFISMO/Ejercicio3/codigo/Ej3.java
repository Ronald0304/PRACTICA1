//3. Un restaurante organiza a su personal mediante las siguientes clases:
//a) Instanciar 1 Cocinero, 2 objetos Mesero y 2 objetos Administrativo.
//b) Sobrecargar el método SueldoTotal para mostrar el sueldo total, sumándole las horas extra, considerando el sueldo por hora y la propina 
//en caso de los meseros. 
//c) Sobrecargar el método para mostrar a aquellos Empleados que tengan SueldoMes igual a X
class Cocinero {
    private String nombre;
    private int sueldoMes;
    private int horasExtra;
    private float sueldoHora;

    public Cocinero(String nombre, int sueldoMes, int horasExtra, float sueldoHora) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
    }

    public void SueldoTotal() {
        float total = sueldoMes + (horasExtra * sueldoHora);
        System.out.println("Cocinero " + nombre + " - Sueldo Total: " + total);
    }

    public void SueldoTotal(int sueldoFiltro) {
        if (sueldoMes == sueldoFiltro) {
            System.out.println("Cocinero " + nombre + " - SueldoMes igual a " + sueldoFiltro);
        }
    }
}

class Mesero {
    private String nombre;
    private int sueldoMes;
    private int horasExtra;
    private float sueldoHora;
    private float propina;

    public Mesero(String nombre, int sueldoMes, int horasExtra, float sueldoHora, float propina) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
    }

    public void SueldoTotal() {
        float total = sueldoMes + (horasExtra * sueldoHora) + propina;
        System.out.println("Mesero " + nombre + " - Sueldo Total: " + total);
    }

    public void SueldoTotal(int sueldoFiltro) {
        if (sueldoMes == sueldoFiltro) {
            System.out.println("Mesero " + nombre + " - SueldoMes igual a " + sueldoFiltro);
        }
    }
}

class Administrativo {
    private String nombre;
    private float sueldoMes;
    private String cargo;

    public Administrativo(String nombre, float sueldoMes, String cargo) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.cargo = cargo;
    }

    public void SueldoTotal() {
        System.out.println("Administrativo " + nombre + " - Sueldo Total: " + sueldoMes);
    }

    public void SueldoTotal(int sueldoFiltro) {
        if (sueldoMes == sueldoFiltro) {
            System.out.println("Administrativo " + nombre + " - SueldoMes igual a " + sueldoFiltro);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Cocinero c1 = new Cocinero("Carlos", 3000, 10, 50);
        Mesero m1 = new Mesero("Ana", 2800, 8, 40, 200);
        Mesero m2 = new Mesero("Luis", 2900, 5, 45, 150);
        Administrativo a1 = new Administrativo("Sofía", 3200, "Contadora");
        Administrativo a2 = new Administrativo("Jorge", 3200, "RRHH");

        System.out.println("------ Sueldos Totales ------");
        c1.SueldoTotal();
        m1.SueldoTotal();
        m2.SueldoTotal();
        a1.SueldoTotal();
        a2.SueldoTotal();

        System.out.println("\n---- Empleados con sueldo del Mes = 3200 ---");
        c1.SueldoTotal(3200);
        m1.SueldoTotal(3200);
        m2.SueldoTotal(3200);
        a1.SueldoTotal(3200);
        a2.SueldoTotal(3200);
    }
}
