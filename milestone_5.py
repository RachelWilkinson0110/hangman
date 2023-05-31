
import random

#Creating a function which generates a random choice from a given sequence

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
        r=[]
        guess=guess.lower()
        if guess in self.word:
            print(f'Good guess, {guess} is in the word!')
            for index, char in enumerate(self.word):
                if char == guess:
                    r.append(index)
            
            for i in r:
                self.word_guessed = self.word_guessed[:i] + guess + self.word_guessed[i+1:]
                self.num_letters = self.num_letters -1
            print(self.word_guessed)
            
            if self.num_letters==0:
                print(f'Congratulations, you have won the game. The word is {self.word}')
                quit()
            
        else:
            print(f"{guess} is not in the word. Please try again")
            self.num_lives= self.num_lives-1
            print(f'You have {self.num_lives} lives left')
            if self.num_lives==0:
                print('You lost')
                quit()
        


    def ask_for_input(self):
        while True:
            guess=input("Please enter a single letter: ")
            
            if len(guess) != 1 or guess.isalpha()==False:
                    print("Invalid letter. Please enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                    print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses += guess
                print(f"list of guesses: {self.list_of_guesses}")

        
def play_game(word_list):
    num_lives=5,
    game=Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives ==0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives >= 0 and game.num_letters==0:
            print("Congrtaultaions, you have won the game!")

if __name__ == '__main__':
    word_list=['apple', 'grapes', 'banana', 'pear', 'melon']
    play_game(word_list)

        
