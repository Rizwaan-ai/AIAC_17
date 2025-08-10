def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Temperature Conversion Program")
    print("Choose conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
    elif choice == '3':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_kelvin(c):.2f}K")
    elif choice == '4':
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K = {kelvin_to_celsius(k):.2f}°C")
    elif choice == '5':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_kelvin(f):.2f}K")
    elif choice == '6':
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K = {kelvin_to_fahrenheit(k):.2f}°F")
    else:
        print("Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()

    while True:
        main()
        again = input("\nDo you want to perform another conversion? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting program. Goodbye!")
            break
