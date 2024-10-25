import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Take a guess from the player
            guess = int(input("Take a guess: "))
            attempts += 1
            
            # Check the player's guess
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when the correct number is guessed
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
