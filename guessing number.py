import random as r
low_num=1
high_num=100
ans=r.randint(low_num,high_num)
guess=0
is_running=True
print('Python NUmber Guessing Game ')
print(f'Select Number between {low_num} and {high_num}')

while is_running:

    gus=input('Enter  Number Guess: ')

    if gus.isdigit():
        gus=int(gus)
        guess= guess+1
        if gus > high_num or gus<low_num:
            print('Number is out of range')
            gus = input('Enter  Number Guess: ')
        elif gus< ans:
            print('Too Low')
        elif gus > ans:
            print('Too High')
        else:
            print('Correct !!!!! The ans is ',gus)
            print("Your Guess attempts",guess)
            is_running=False

    else:
        print('Invalid Input')
        print(f'PLease Enter Number between {low_num} and {high_num}')




