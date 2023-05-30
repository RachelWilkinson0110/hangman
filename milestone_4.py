
import random

class Hangman:

#initilaising attributes
    def __init__(self,word_list, num_lives=5):
        self.word_list=word_list
        self.num_lives=5

        self.word=random.choice(word_list)
        self.word_guessed='_'*len(self.word)
        self.num_letters=self.word_guessed.count('_')
        self.list_of_guesses= []

        print(f'The mystery word has {self.num_letters} letters - {self.word_guessed}')
        
        
#Creating methods

    def check_guess(self,guess):
        guess=guess.lower()
        if guess in self.word:
            print(f'Good guess, {guess} is in the word!')
            for i in range(0, len(self.word)):
                if self.word[i]==guess:
                    result=i
                    print(result)
                    self.word_guessed=self.word_guessed.replace(self.word_guessed[result], guess, 1)
            print(self.word_guessed)
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
                self.check_guess(guess)
                self.list_of_guesses += guess
                print(self.list_of_guesses)

word_list=['apple','banana']
test=Hangman(word_list,num_lives=5)

test.ask_for_input()
