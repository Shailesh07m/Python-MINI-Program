
foods=[]
prices=[]
total=0

while True:
    food=input("Enter food:(Q to quit): )")
    if food == "Q" or food == "q" :
        break
    else:
        price=float(input(f"Enter price of {food}: ₹ "))
        foods.append(food)
        prices.append(price)

print('--------Your Cart --------')
for i in foods:
    print(i)

for i in prices:
    total+=i

print(f'Total Price: ₹ {total}')