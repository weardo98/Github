'''
In this example, we want the index of the data source to be an ID number from
the file instead of a sequence of integers starting with zero.

That means the rows will be entries in a dictionary, where the keys are ID#'s.

Thus, the data will be a dictionary of dictionaries.

The first ROW is the headings, and the first COLUMN is the ID number. We
will read that information to structure the data.
'''

import csv
f = open('example_id.csv')
reader = csv.reader(f)

headings = reader.next() #First row of the CSV is the headings.

d = {} #Create blank dictionary; this will gain a "sub-dictionary" for each row

for row in reader: #Loop through the remaining lines in the CSV file
    dictionary = {} #create a blank dictionary for this row
    #enumerate() numbers the items to help with list indexing inside the loop
    for index, key in enumerate(headings): #Loop through the headings list
        dictionary[key] = row[index] #Add column data to the dictionary
    d[row[0]] = dictionary #add the dictionary, with row[0] data as the key.
    
f.close() #Windows can't do stuff with your file as long as Python has it open.

def avg_grade(dictionary):
    sum = 0
    for key in d:
        num = int(d[key]['grade'])
        sum += num
    return float(sum)/len(d)
    
    