# Important necessary modules
import random
import time

# Pick a number between 1 and 100
number = random.randint(1,100)

def intro():
    print("May I Ask you for your name?")
    # declaring name variable global so it can be accessed outside the function
    global name
    name = input() #asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print("\nThis is an {} number".format(x))
    time.sleep(.5)
    print("Go Ahead. Guess!")

def pick():
    guessesTaken = 0

    #if the number of guesses is less than 6
    while guessesTaken < 6:
        time.sleep(.25)
        #inserts the place to enter guess
        enter=input("Guess: ")

        #check if a number was entered
        try:
            #stores the guess as an integer instead of a string
            guess = int(enter)
            guessesTaken += 1

            if guess < number:
                print("Your guess is too low")

            if guess > number:
                print("Your guess is too high")

            if guess == number:
                break

        except:
            print("Please enter a number")

    if guess == number:
        print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses!")

    if guess != number:
        print("Nope. The number I was thinking of was " + str(number))

# calling functions
intro()
pick()