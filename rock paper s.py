import random as r
options=('rock','paper','scissors')
player=None
comp=r.choice(options)

playing=True
while playing:
    player = None
    comp = r.choice(options)
    while player not in options:
        player = input('Enter your choice:(rock,paper,scissors) :')

    if player == comp:
        print('Draw')
    elif player == 'rock' and comp == 'scissors':
        print('You win')
    elif player == 'paper' and comp == 'rock':
        print('You Win')
    elif player == 'scissors' and comp == 'paper':
        print('You Win')
    else:
        print('You Lose')

    print(f'Player : {player}')
    print(f'Computer : {comp}')
    again = input('Do you want to play again?(yes/no) ').lower()
    if not again == 'y':
        playing=False


print('Thanks for playing')