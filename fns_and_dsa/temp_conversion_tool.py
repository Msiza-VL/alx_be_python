FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
    
    try:
        temeparature = int(input("Enter the temperature to convert: "))
        c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if c_or_f == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif c_or_f == "F":
            result2 = convert_to_celsius(temeperature)
            print({temperature}°F is {result2}°C)
        else:
            print(f"Invalid temperature. Please enter a numeric value.")
        except:
            print(f"Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()