import random
def spin():
    symbols=[ '🍒', '🍉', '🍋' ,'🔔' ,'⭐']
    return[ random.choice(symbols) for _ in range(3)]
def print_row(row):
    print('--------------------')
    print(" | ".join(row))
    print('--------------------')
def get_payout(row,bet):
    if row[0]== row[1] == row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🍉':
            return bet*4
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='🔔':
            return bet*6
        elif row[0]=='⭐':
            return bet*10
        else:
            return 0
    else:
            return 0
def main():
    balance=10000
    print('----------------------------------')
    print('Welcome to Python Slots')
    print('Symbols : 🍒 🍉 🍋 🔔 ⭐')
    print('----------------------------------')

    while balance > 0:
        print(f'Current Balance: ₹ {balance}')
        print('----------------------------------')
        bet= input('Enter your bet: ')
        if not bet.isdigit():
            print('Please enter a Valid Number')
            continue

        bet = int(bet)
        if bet > balance:
            print('Insufficient Balance')
            continue
        if bet <= 0:
            print('Bet must be greater than 0')
            continue
        balance  -= bet
        row = spin()
        print('Spinning ')
        print_row(row)
        payout=get_payout(row,bet)

        if payout >0:
            print(f'You Won ₹ {payout}')
        else:
            print(f'You Lost')

        balance = balance + payout




if __name__ == '__main__':
    main()