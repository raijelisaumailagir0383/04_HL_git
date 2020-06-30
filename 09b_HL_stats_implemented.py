# HL component 9b - End Game Stats

# To Do
# Set up Game Play list with each round's results
# Set up average, best and worst scores (see 09b Stats_experiment)


SECRET = 7
GUESSES_ALLOWED = 4
rounds = int(input("How many rounds? "))   # replace with int check
game_stats = []

num_won = 0
rounds_played = 0

if __name__ == '__main__':
    while rounds_played < rounds:
        guess = ""
        guesses_left = GUESSES_ALLOWED

        while guess != SECRET and guesses_left >= 1:

            guess = int(input("Guess: "))   # replace this with function call in due course
            guesses_left -= 1

            if guesses_left >= 1:

                if guess < SECRET:
                    print("Too high, try a lower number. Guesses left: {}".format(guesses_left))

                elif guess > SECRET:
                    print("Too low, try a higher number.  Guesses left: {}".format(guesses_left))
            else:
                if guess < SECRET:
                    print("Too high!")
                elif guess > SECRET:
                    print("Too low!")

        if guess == SECRET:
            if guesses_left == GUESSES_ALLOWED - 1:
                print("Amazing! You got it in one guess")
            else:
                print("Well done, you got it in {} guesses".format(GUESSES_ALLOWED - guess))
            num_won += 1
        else:
            print("Sorry - you lose this round as you have run out of guesses")
            guesses_left -= 1   # penalty point for losing

        game_stats.append(GUESSES_ALLOWED - guesses_left)
        print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1

# print each round's outcome...
print()
print("*** Game Scores***")
list_count = 1
for item in game_stats:

    # indicates if game has been won or lost
    if item > GUESSES_ALLOWED:
        status = "lost, ran out of guesses"
    else:
        status = "won"

    print("Rounds {}: {} ({})".format(list_count, item, status))
    list_count += 1

# Calculate (and then print) game statistics
game_stats.sort()
best = game_stats[0]   # first item in sorted list
worst = game_stats[-1] # last item in sorted list
average = sum(game_stats)/len(game_stats)

print()
print("*** Summary Statistics***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f".format(average))