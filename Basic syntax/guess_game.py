# Guess the numbers game

# Import random module to create random numbers of randint function
import random

#Greet player with statement and ask for name
print("Hello what is your name?")
name = input()

# String concatonation to greet the player by name 
print("Well, " + name + " I am thinking of a number between 1 and 20.")

# Generate secret number using randint, define the limits of random number geneated
secretNumber = random.randint(1, 20)

# Ask player to guess up to six times for correct random number
# Use two argument form of the range function
# Store guess as variable with int value
# If guess is less or greater than the secret number inform the player
# If the number selected is correct break out of the loop
for guessesTaken in range(1, 7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

# If the guess is correct convert number of guesses taken into a string and print
if guess == secretNumber:    
    print("Congratulations " + name + " you have selected the correct number using " + str(guessesTaken) + " guesses")
else:
    print("Sorry you have run out of chances,  the correct number was " + str(secretNumber))



