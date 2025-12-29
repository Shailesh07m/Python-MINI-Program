import random
def roll_dice():
    num=random.randint(1,6)
    print(f'Dice rolled: {num}')
    if num==6:
        print('You Win!!')
    else:
        print('Try Again')
