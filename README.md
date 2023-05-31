# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Milestone 2
In this section we used the random module to choose a fruit from a list of defined fruit.
I have also used the input function to request a single letter input from the user. To validate that this is a single letter I have used the len function (ensuring it is 1) and the isaplha() function (ensuring that the return is True).

Milestone 3
In this section we have created two functions. The funciton ask_for_input will ask the user to enter a single letter. This function will also validate this input using the methods added in milestone 2. The funciton check_guess will check and inform the user if the letter they have guessed is in the random word.

Milestone 4
In this section we created the class Hnagman. We also intialised the parameters and attributes using the __init__ command.
Next we updated the functions that we created in the previous milestones so that they can act as methods of this class.

Milestone 5
In this section I made updates to how I replace the dahses - "_" in the word_guessed with the user input - In milestone 4 the letters were being populated in any order meaning they were not showing the user the correct position of their guess. This update has corrected this.

I have also added some conditions of the game, for example if the user uses all their lives the game will end and they will receive a message to that affect. Alternatively if they win, the game will end with a congratulatory note.




