menu={"pizza":300 ,
      "nachos":450,
      "popcorn":600,
      "fries":250,
      "chips":300,
      "pretzels":300,
      "soda":350,
      "lemonade":425
      }

cart=[]
total=0
print('--------------MENU------------------')
print("   Item                             Price ₹")
for key,value in menu.items():
   print(f"   {key}:                        ₹ {value}")
print('-------------------------------------')
while True:
    food=input('Select an Item (Q to quit): )').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print('------------Your Order----------------')
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")


print()
print(f"Total: {total}")
