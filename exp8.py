def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius} degrees Celsius is equal to {result:.2f} degrees Fahrenheit.")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to {result:.2f} degrees Celsius.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
