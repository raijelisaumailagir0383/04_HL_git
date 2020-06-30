# HL component 4 - compares users guess with secret number

# To Do
#  Set up number of guesses
# Count # of guesses
# if user runs out of gusses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

SECRET = 7
GUESSES_ALLOWED = 4

# initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >=1:

     guess = int(input("Guess: "))  # replace this with function call in due course
     guesses_left -= 1

     # If user has guesses left...
     if guesses_left >= 1:
         while guess != SECRET:
            input("Too high, try a lower number. Guesses left: {}".format(guesses_left))

     elif guess > SECRET:
      input("Too low, try a higher number. Guesses left: {}".format(guesses_left))

     # if the user is out of guesses
     else:
         if guess < SECRET:
             print("Too low!")
         elif guess > SECRET:
             print("Too high!")

if guess == SECRET:
     # If user guessed right the first time...
     if guesses_left == GUESSES_ALLOWED - 1:
         print("Amazing! You got it in one guess")
     # If user has had more than one guess...
     else:
         print("Well done, you got it in {} guesses".format(len(guesses_left)))
     num_won += 1
# User has run out of guesses (and loses the game)
else:
    print("Sorry - you lose this round as you have run out of guesses")


