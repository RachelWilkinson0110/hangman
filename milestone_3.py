word='apple'
def check_guess(guess):
    guess=guess.lower()
    if guess in word:
        print(f'Good guess, {guess} is in the word!')
    else:
        print(f"{guess} is not in the word. Please try again")


def ask_for_input():
    while True:
        guess=input("Please enter a single letter: ")
        if len(guess) == 1 and guess.isalpha() is True:
            break
        else:
            print("Invalid input. Please enter a single alphabetical character")
    check_guess(guess)

ask_for_input()



