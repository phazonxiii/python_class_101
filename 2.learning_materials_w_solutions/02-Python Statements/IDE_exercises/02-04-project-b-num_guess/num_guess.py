# Author: Brandon Hoffman
# Date: 10/05/2020
# Description: Guessing game that takes a number to guess and has user contiously 
#              make guesses till they get the answer correct



def check_guess(solution, guess):   
    """
    Takes in a solution and guess parameters as integers
    Returns the count of attempts to make the guess equal solution
    """

    if guess == solution:
        print("You guessed it in 1 try.")
    else:
        number_of_guesses = 1
        
        while guess != solution:
            if guess > solution:
                print("Too high - try again:")
                guess = int(input())
            if guess < solution:
                print("Too low - try again:")
                guess = int(input())

            number_of_guesses += 1

        print("You guessed it in", number_of_guesses, "tries.")

def main():
    """
    Main program to be executed
    """
    print("Enter the number for the player to guess.")
    solution = int(input())

    print("Enter your guess.")
    guess = int(input())

    check_guess(solution, guess)

main()