#########################   EXERCICE PRATIQUE PYTHON   #############################

# EX1 factorielle#


n = int(input("entrer un nbr entier : "))
f = 1

for i in range(1, n+1):
    f = f * i
print("le factorielle de", n, "est", f)

##############################################################################

# EX2 degre  fahreheit#

c = float(input("Saisir la temperature en C : "))

F = c * 9/5 + 32
print("La temperature en fahreheit : ", F)

#############################################################################

# EX3 RANDOM GUESS#
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
                print(f"Congratulations! You guessed the number in {
                      attempts} attempts.")
                break  # Exit the loop when the correct number is guessed
        except ValueError:
            print("Please enter a valid number.")


guess_the_number()

################################################################################

# EX4 PLUS GRAND DE 3 NBR#

nbr1 = int(input("entrer le 1er nbr : "))
nbr2 = int(input("entrer le 2eme nbr : "))
nbr3 = int(input("entrer le 3eme nbr : "))

plus_grand_nbr = nbr1

if nbr2 > nbr1:
    plus_grand_nbr = nbr2

if nbr3 > plus_grand_nbr:
    plus_grand_nbr = nbr3

print(f"le plus grand nbr est : {plus_grand_nbr} ")

###############################################################################

# EX5 VOYELLES ET CONSONNES#

# La méthode isalpha() est une méthode intégrée en Python qui vérifie si un caractère est une lettre.#
# Voici ce qu'elle fait : #
# Retourne True si le caractère est une lettre (A-Z ou a-z)#
# Retourne False sinon (espaces, chiffres, ponctuation, etc.)#

voyelles = "aeiouyAEIOUY"

phrase = input("entrer une phrase : ")

nbr_voyelles = 0
nbr_consonnes = 0

for caractere in phrase:
    if caractere.isalpha():
        if caractere in voyelles:
            nbr_voyelles += 1
        else:
            nbr_consonnes += 1

print(f"Les nombres des voyelles dans la phrase est : {nbr_voyelles} ")
print(f"Les nombres des consonnes dans la phrase est : {nbr_consonnes} ")
print(f"Le nombre total des voyelles et les consonnes est :  {nbr_voyelles + nbr_consonnes} ")

##################################################################################################

