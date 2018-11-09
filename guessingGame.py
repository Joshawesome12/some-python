import random

number = random.randint(1,99)

guesses = 0

while guesses < 5:
    guess = int(raw_input("Enter and integer from 1 to 99:"))
    guesses += 1
    print "This is your %d guess" %guesses

    if guess < number:
        print "Your guess is low"
    elif guess > number:
        print "Your guess is high"
    elif guess == number:
        # break
        guesses = str(guesses)
        print "You guessed it in :", guesses + "guesses"

if guess != number:
        number = str(number)
        print "The secret number was", number
