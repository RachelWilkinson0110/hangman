
import random
class Hangman:

#initilaising attributes
    def __init__(self,word_list, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives

        self.word=word
        self.word_guessed='_'*len(self.word)
        self.num_letters=num_letters
        self.list_of_guesses= []
        
#Creating methods

    def check_guess(self,guess):
        guess=guess.lower()
        if guess in self.word:
            print(f'Good guess, {guess} is in the word!')
            for char in word:
                if char==guess:
                    self.word_guessed.append(char)
                else:
                    self.word_guessed.append('_')
                return self.word_guessed
            self.num_letters = self.num_letters -1
        else:
            print(f"{guess} is not in the word. Please try again")
            self.num_lives= self.num_lives-1
            print(f'You have {self.num_lives} left')


    def ask_for_input(self):
        while True:
            guess=input("Please enter a single letter: ")
            if len(guess) != 1 and guess.isalpha() is False:
                print("Invalid letter. Please enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                check_guess(guess)
                self.list_of_guesses += guess

