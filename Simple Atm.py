def Atm():
    pin="2468"
    balance=2000
    entered_pin=input("Enter the Pin: ")
    if entered_pin != pin:
        print("Invalid Pin. Access Denied.")
        exit()

    while True:
        choice = int(input("""
            1.Check Balance
            2.Deposit
            3.Withdraw
            4.Exit

            Enter your choice:"""))

        match choice:
            case 1:
                print("Your balance is: ", balance)
            case 2:
                amount = int(input("Enter the amount: "))
                balance += amount
                print("Your balance is: ", balance)
            case 3:
                amount = int(input('Enter the amount to withdraw: '))
                if amount <= balance:
                    balance -= amount
                    print("Your balance is: ", balance)
                else:
                    print('insufficient funds')
            case 4:
                print('Thank you for your using our services.')
                break
            case _:
                print("Invalid choice.")

