'''
histogram_age_income.py 
reads data from the age_income_feb14.csv
and creates two histograms: the age distribution and the income 
distribution. The data are from U.S. Census Bureau's February 2014 
Current Population Survey. 

(c) 2014 Project Lead The Way
'''
import matplotlib.pyplot as plt

# A generic helper function for matplotlib.pyplot graphics
def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Georgia')
        item.set_fontsize(16)

###
# Get the income/age data from CSV
###
# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'age_income_feb14.csv')
datafile = open(filename,'r')
data = datafile.readlines()

####
# Transform the data from strings to signed integers
####
ages=[]
incomes=[]
for line in data[3:]: # Omit 0, 1, 2 because _______
    age, income = line.split(',')

    # ___________ the age data
    ages.append(int(age))

    # __________ the income data
    if '-' in income:
        # Do not use the first 3 characters: space, -, and $
        # and do not use the last character: \n
        incomes.append(-1*int(income[3:-1]))
    else:
        # Do not use the first 2 characters: space and $
        # and do not use the last character: \n
        incomes.append(int(income[2:-1]))         

###
# Create the histograms
###

# Histogram 1
fig_age, ax  = plt.subplots(1, 1)
a = ax.hist(ages, color='cyan', bins=range(15, 115, 10)) 
ax.set_title('Age Distribution in Feb 2014 U.S. Sample')
ax.set_xlabel('Age (yrs)')
ax.set_ylabel('Frequency (# people)')
make_PLTW_style(ax)
fig_age.show()

print sum(incomes)
# Histogram 2
fig_income, ax  = plt.subplots(1, 1)
ax.hist(incomes, color='#7777ff', bins=200)
ax.set_xlim(0,105000)
ax.set_title('Income Distribution in Feb 2014 U.S. Sample')
ax.set_xlabel('Household income ($/yr)')
ax.set_ylabel('Frequency (# people)')
make_PLTW_style(ax)
fig_income.show()