'''
CSV is "comma separated values." It is a human readable text file format.

Python can easily read CSV. First you open the file, then create a 
csv.reader object that you can loop through.

The last line creates the "datra" list by looping through the reader object.

Try indexing the "data" object. Examples: data[0] or data[1][2]

"data" is a list of lists. Each of the rows is its own list of columns.
'''

import csv
f = open('Bitcoin price.csv')
reader = csv.reader(f)

data = []
reader.next()
#reader.next()
#for row in reader:

for i in range(32):
    row = reader.next()
    data += [row]



#f.close() #Windows can't do stuff with your file as long as Python has it open.