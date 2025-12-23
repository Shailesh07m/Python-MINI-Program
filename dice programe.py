import random as r



# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│       ● │",
       "│    ●    │",
       "│ ●       │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘")
}

dice=[]
total=0
num_dice=int(input('How many dice? :'))

for die in range(num_dice):
 dice.append(r.randint(1,6))

# for die in range(num_dice):
#     for line in dice_art.get(dice[die]):
#         print(line,end="")

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()

for die in dice:
    total+=die
print(f"Total : {total}")