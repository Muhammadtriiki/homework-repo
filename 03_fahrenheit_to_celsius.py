def calculation(degrees, conversion_type):
    if conversion_type == "fahrenheit":
        degrees_celsius = (degrees - 32) * 5.0 / 9.0
        return degrees_celsius
    elif conversion_type == "celsius":
        degrees_fahrenheit = (degrees * 9.0 / 5.0) + 32
        return degrees_fahrenheit
    else:
        return "incorrect measurement"


choice = input("which degree you want to convert to fahrenheit or celsiu ? ")

if choice.lower() == "fahrenheit":
    try:
        degrees_fahrenheit = float(input("input fahrenheit degree to convert it into Celsius: "))
        result = calculation(degrees_fahrenheit, "fahrenheit")
        print(f" Tempreture:{degrees_fahrenheit}F = {result}C")
    except ValueError:
        print("invalid input. Please enter a number.")
elif choice.lower() == "celsius":
    try:
        degrees_celsius = float(input("input celsius degree to convert it into Fahrenheit: "))
        result = calculation(degrees_celsius, "celsius")
        print(f" Tempreture: {degrees_celsius}C = {result}F")
    except ValueError:
        print("invalid input. please enter a number.")
else:
    print("incorrect measurement")
