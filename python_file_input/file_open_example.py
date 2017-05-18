f = open('fruits.txt')
fruits_raw = f.readlines()

fruits = []
for row in fruits_raw:
    fruits += [row.strip()]

f.close() #Windows can't do stuff with your file as long as Python has it open.


'''
When you use this simple method, the rows will contain '\n' characters, 
which are line breaks.
You can get rid of those and other white spaces at the start and end of 
lines using the string.strip() method. The following code loops through your 
raw list and strips the white space out of each row. 

In your Python window, look at the items from fruits by indexing them.
For example, fruits[0] or fruits[3:5]

Now you can easily loop through the fruits, or select a random fruit.

If you want to add or remove fruits from the list, just edit the text file, 
and the code will still work. This makes it easy to change your data.
'''

