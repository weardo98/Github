import csv
import random as r
Q = []
with open('pubtrivia.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        Q += [row[0].split('?')]

for item in Q:
    item[1] = item[1][1:]

def ask():
    x = r.choice(range(len(Q)))
    print Q[x][0],"?"
    answer = raw_input()
    if answer == Q[x][1]:
        print 'Congratulations! Your answer is correct.'
    else:
        print 'Sorry, your answer is incorrect.'
        print 'The correct answer is:', "\n", Q[x][1]