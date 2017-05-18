import time
import urllib
import random
words = urllib.urlopen('http://davidbau.com/data/words').read().split()
def num(x):
    nums = range(x)
    for i in range(x):
        time.sleep(0.1)
        print nums[i]
def lan():
    words = ('computer','hard drive','graphics')
    for i in range(3):
        print len(words[i])
        
def dat(x,y):
    z = y + 1
    print range(x,z)

def hangman():
    print "Welcome to Hangman you have 8 guesses!"
    y = random.choice(words)
    guessed = ""
    trys = 8
    while (trys > 0):
        g = raw_input("Type a Guess: ")
        guessed += g
        h = hint(guessed,y)
        trys -= 1
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