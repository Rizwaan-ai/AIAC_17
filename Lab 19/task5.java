public class Car {
    // 1. Attributes with explicit type declarations
    private String brand;
    private String model;
    private int year;
    // 2. Constructor (matches the class name)
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }
    // 3. Method to display details
    public void displayDetails() {
        System.out.println("--- Java Output ---");
        System.out.println("Car Details:");
        System.out.println("Brand: " + this.brand);
        System.out.println("Model: " + this.model);
        System.out.println("Year: " + this.year);
    }
    // Main method to create an object and run the code
    public static void main(String[] args) {
        // --- Object Creation and Method Call ---
        // 1. Create an object (instance of the Car class)
        Car myJavaCar = new Car("Toyota", "Corolla", 2020);
        // 2. Call the method
        myJavaCar.displayDetails();
    }
}