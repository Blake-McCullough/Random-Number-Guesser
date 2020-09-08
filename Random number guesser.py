import random
print("Random number guesser by Blake McCullough")
random_number = random.randint(1,100)
won = False
turns = 0
while not won:
    try:
        guess = input("Enter a number between 1 and 100: ")
        guess = int(guess)
    except ValueError:
        print("The following is not a valid number", guess)
        print("Please try again.")
        continue
    turns += 1
    if random_number == guess:
        print("You won!")
        print("Number of turns you have used: ", turns)
        won = True
    elif random_number > guess:
        print("Your guess was low, please enter a higher number")
    else:
        print("Your guess was high, please enter a lower number")
