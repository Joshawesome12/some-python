#import time module
import time

#welcome user

def hangman() :
    name = raw_input("what is your name?")

    print "Hello, " + name, "Time to play hangman!"

    print ""

    # wait for 1 second
    time.sleep(1)

    print "Start guessing..."
    time.sleep(5)

    #Set the secret
    word = "secret"

    #create a variable with an empty value
    guesses = ''

    #determine number of turns
    turns = 10

    #Create while loop

    #check if the number of turns are more than zero
    while turns > 0:

        #make counter that starts with zero
        unguessed = 0

        #for every character in secret_word
        for char in word:
            #see if the character is in the players guess
            if char in guesses:
                #print then out the character
                print char

            else:
                #if not found print a dash
                print "_"

                #Increase the unguessed counter by one
                unguessed += 1

        #if unguessed is equal to zero
        if unguessed == 0:
            #print you won
            print "You won!"
            #exit script
            break

        #ask the user to guess a character
        guess = raw_input("guess a character:")

        #set the players guess to guesses
        guesses += guess

        #if the guess is not found in the secert word
        if guess not in word:
            #turns decreases by 1
            turns -= 1

            #print wrong
            print "Wrong"

            #turns left
            print "You have", + turns, "more guesses"

            #if the turns are equal to zero
            if turns == 0:
                #print you loose
                print "You loose"

    again()


def again():
    play_again = raw_input("Do you want to play again?")
    if play_again == "yes":
        hangman();

    elif play_again == "no":
        print "See you later!"
        return

    elif play_again != "yes" or "no":
        print "Lets try that again! Try typing yes or no."
        again();

hangman();
