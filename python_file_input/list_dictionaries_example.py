'''
CSV is "comma separated values." It is a human readable text file format.

Python can easily read CSV. First you open the file, then create a 
csv.reader object that you can loop through.

The last line creates the "data" list by looping through the reader object.

Try indexing the "data" object. Examples: data[0] or data[1][2]

"data" is a list of lists. Each of the rows is its own list of columns.
'''

import csv
f = open('example.csv')
reader = csv.reader(f)
headings = reader.next() #First row of the CSV is the headings.
d = [] #Create blank list of dictionaries
for row in reader: #Loop through the remaining lines in the CSV file
    dictionary = {} #create a blank dictionary for this row
    #enumerate() numbers the items to help with list indexing inside the loop
    for index, key in enumerate(headings): #Loop through the headings list
        dictionary[key] = row[index] #Add each column to the dictionary
    d += [dictionary] #add the dictionary to the list
        
    
f.close() #Windows can't do stuff with your file as long as Python has it open.
