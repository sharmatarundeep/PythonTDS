P# This is a fun guess the number game
import random # as we need to come up with a random number, we would need random module

print("Hi, welcome to the Guess the number game...\nWhat is your name?")
name = input() # Take user input

print("Well " + name + ", I am thinking of a number between 1 to 20, can you guess it?")
secretnumber = random.randint(1,20) # Generate a random number and store it to compare later
#Ask player to guess 5 times. 5 is the max chances player have to guess it right
for i in range (5):
    print("Take a guess")
    guess = int(input())
    if guess > secretnumber:
        print("Your guess is too high")
    elif guess < secretnumber:
        print("Your guess is too low")
    else:
        break # this condition is for correct guess

if guess == secretnumber:
    print("Good job, " + name + ". You guess it right in " + str(i+1)+ " times")
else:
    print("Sorry, you lost all your " + str(i+1) + " chances. I was thinking about " + str (secretnumber))
