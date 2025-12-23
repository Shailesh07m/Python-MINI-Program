principle=0
rate = 0
time =0
while True:
    principle=float(input("enter principle amt:"))
    if  principle <= 0 :
        print('Principle Cant be less or equal to 0')
    else:
        break

while True:
    rate = float(input("enter rate of interest:"))
    if rate <= 0:
        print('Rate Cant be less or equal to 0')
    else:
        break

while True:
    time = float(input("enter Time iin year:"))
    if time <= 0:
        print('Principle Cant be less or equal to 0')
    else:
        break


total = principle *pow((1+ rate /100),time)
print(f'Balance After {time} Years: {total:.3f}')