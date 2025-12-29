import atm
import game
import Utility

while True:
    print("\n=========== MAIN MENU ===========")
    print("1. ATM")
    print("2. Game")
    print("3. Utility")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if atm.access():
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")

            atm_choice = int(input("Enter your choice: "))

            if atm_choice == 1:
                atm.check_balance()
            elif atm_choice == 2:
                amt = int(input("Enter amount: "))
                atm.deposit(amt)
            elif atm_choice == 3:
                amt = int(input("Enter amount: "))
                atm.withdraw(amt)
        else:
            print("Wrong PIN,Access Denied")

    elif choice == 2:
        game.roll_dice()

    elif choice == 3:
        print("\n1. Square Root")
        print("2. Show Time")

        util_choice = int(input("Enter choice: "))

        if util_choice == 1:
            n = int(input("Enter number: "))
            Utility.square_root(n)
        elif util_choice == 2:
            Utility.show_time()

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
