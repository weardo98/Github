import urllib
import random
words = urllib.urlopen('http://davidbau.com/data/words').read().split()
def hangman():
    print "Welcome to Hangman you have 10 guesses!"
    y = random.choice(words)
    guessed = []
    trys = 10
    while (trys > 0):
        g = raw_input("Type a Guess: ")
        guessed += g
        h = hint(guessed,y)
        trys -= 1
        print "letters guessed" + str(guessed)
        print h
        if h == y:
            print "yay you solved the puzzle"
            print "use CTRL+R to restart"
            break
        if (trys == 0) :
            print "try again next time"
            print "use CTRL+R to restart"
def hint(x,y):
    hint = ""
    for letter in y:
       if letter in x:
           hint += letter
       else:
           hint += " _ "
    return hint 
hangman()