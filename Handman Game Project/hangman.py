import random
from wordlist import words # list of words to guess

# Dictionary that stores Hangman drawings
# O is used instead of 0 for the head
hangman_art = {
    0: (
        "     ",
        "     ",
        "     "
    ),
    1: (
        "  O  ",
        "     ",
        "     "
    ),
    2: (
        "  O  ",
        "  |  ",
        "     "
    ),
    3: (
        "  O  ",
        " /|  ",
        "     "
    ),
    4: (
        "  O  ",
        " /|\\ ",
        "     "
    ),
    5: (
        "  O  ",
        " /|\\ ",
        " /   "
    ),
    6: (
        "  O  ",
        " /|\\ ",
        " / \\ "
    )
}


# Displays hangman drawing based on wrong guesses
def display_hangman_art(wrong_guesses):
    print("-------------------------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-------------------------------------")


# Displays the current hint (underscores and guessed letters)
def display_hint(hint):
    print("Word:", " ".join(hint))


# Displays the final answer
def display_ans(ans):
    print("Answer:", " ".join(ans))


def main():
    # Randomly select a word
    ans = random.choice(words).lower()

    # Create hint list with underscores
    hint = ["_"] * len(ans)

    wrong_guesses = 0
    guessed_letters = set()  # to avoid repeated guesses
    is_running = True

    while is_running:
        display_hangman_art(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        # Check if letter already guessed
        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        guessed_letters.add(guess)

        # If guess is correct, reveal letter(s)
        if guess in ans:
            for i in range(len(ans)):
                if ans[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        # Win condition
        if "_" not in hint:
            display_hangman_art(wrong_guesses)
            display_ans(ans)
            print("🎉 You win!")
            is_running = False

        # Lose condition
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman_art(wrong_guesses)
            display_ans(ans)
            print("❌ You lose!")
            is_running = False


# Entry point of the program
if __name__ == "__main__":
    main()
