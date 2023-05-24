#Importing the packages and modules we will need to run this code
import random

#Creating a list of my five favourite fruits
word_list=['apple', 'grapes', 'banana', 'pear', 'melon']
#print(word_list)

#Creating a function which generates a random choice from a given sequence

def random_word_choice(list):
    word=random.choice(list)
    print(word)

random_word_choice(word_list)

#Asking the user to enter a single letter
def single_letter_input():
    guess=input("Please enter a single letter: ")
    if len(guess) is 1 and guess.isalpha() is True:
        print("Good guess!")
    else:
        print("Oops, that is not a valid input")

single_letter_input()