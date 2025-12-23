from selectors import SelectSelector

weight=float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K,P): ")
if unit == "P":
    weight = weight * 2.205
    unit="lbs"
    print(f"Your Weight is {round(weight, 3)}{unit} ")
elif unit == "K":
    weight = weight / 2.205
    unit="kgs"
print(f"Your Weight is {round(weight,3)}{unit} ")








