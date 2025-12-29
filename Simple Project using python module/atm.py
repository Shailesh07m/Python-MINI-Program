pin = "1234"
balance = 4000

def access():
    ans = input("Enter PIN: ")
    return ans == pin

def check_balance():
    print(f"Current balance is ₹{balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ₹{amount}")
    else:
        print("Insufficient funds")
