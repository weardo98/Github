def mouse(x,y):
    if x > 20 and x < 100 and y > 20 and y <100:
        return "YAY you're smart"
    else:
        return "Try again"

def report_grade(percent):
    if percent >= 80:
        return "mastery"
    else:
        return "get good"

def vowel(guess,word):
    if guess in word:
        return "correct"
    else:
        return "wrong"

def hint(color):
    secret = ['red','red','yellow','yellow','black']
    if color in secret:
        return "That color is in the secret sequence of colors."
    else:
        return "That color is NOT in the secret sequence of colors."