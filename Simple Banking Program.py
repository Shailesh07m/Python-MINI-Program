def show_balance(balance):
    print(f'Your current balance is ₹ {balance:.2f}')
def deposit():
    amount = int(input('Enter the amount you want to deposit: '))
    if amount < 0:
        print('Please enter a valid amount')
        return 0
    else:
        return amount
def withdraw(balance):
    amount = int(input('Enter the amount you want to withdraw: '))
    if amount > balance:
        print('Insufficient funds')
        return 0
    elif amount < 0:
        print('Please enter a valid amount. Greater than 0')
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print('-----------------------------------------')
        print("Welcome to the Banking Program")
        print('*****************************************')
        print(' 1. Show Balance')
        print(' 2. Deposit')
        print(' 3. Withdraw')
        print(' 4. Exit')
        print('*****************************************')
        choice = input('\nEnter your choice: ')

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
            print('Amount Deposited Successfully')
        elif choice == '3':
            balance -= withdraw(balance)
            print('Amount Withdrawed Successfully')
        elif choice == '4':
            is_running = False
        else:
            print("Please enter a valid choice")

    print('Thank you for using our services ! have a nice day!')

if __name__ == '__main__':
    main()