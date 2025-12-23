unit = input("Enter a Unit of Measurement (C/F) : ")
temp = float(input("Enter Temperature : "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The temperature in Fahrenheit is {temp}°F")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {temp}°C")

else:
    print(f"{unit} is not a valid unit")
