'''
read_feb14_cps.py
Reads a CPS.dat file
using the Jan 2014 Data Dictionary (which will likely apply to all 2014 files)
Creates two CSV files:
    age, income (contained in 'feb_2014_cps_age_income.csv')
    state, household_size (contained in 'feb_2014_cps_state_household_size.csv')
'''

import random


###
# Open the infile and outfile
# To apply to another file than Feb 2014, change these.
####
# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'age_income_feb14.csv')

infilename = os.path.join(directory, 'feb14pub_header.dat') # Use 500-line header; change to use full data set if available
infile = open(infilename,'r')
outfilename1 = os.path.join(directory, 'age_income_feb14pub_header.csv')
outfile1 = open(outfilename1,'w')
outfilename2 = os.path.join(directory, 'household_size_feb14pub_header.csv')
outfile2 = open(outfilename2,'w')
outfile1.write('Age, Income')
outfile2.write('State, Household Size')
source = 'Data from February 2014 Current Population Survey\nRetrieved from thedataweb.rm.census.gov/ftp/cps_ftp.html'
outfile1.write(source)
outfile2.write(source)

####
# Use state code in characters 93-94. 
####
code_93_94={1:'AL',30:'MT',2:'AK',31:'NE',
4:'AZ',	32:'NV',5:'AR',	33:'NH',6:'CA',	34:'NJ',8:'CO',	35:'NM',
9:'CT',	36:'NY',10:'DE',37:'NC',11:'DC',38:'ND',12:'FL',39:'OH',
13:'GA',40:'OK',15:'HI',41:'OR',16:'ID',42:'PA',17:'IL',44:'RI',
18:'IN',45:'SC',19:'IA',46:'SD',20:'KS',47:'TN',21:'KY',48:'TX',
22:'LA',49:'UT',23:'ME',50:'VT',24:'MD',51:'VA',25:'MA',53:'WA',
26:'MI',54:'WV',27:'MN',55:'WI',28:'MS',56:'WY',29:'MO'}
####
# Income code
# Actual meaning of code is an interval
####
code_39_40={1:(-5000,5000), 2:(5000, 7500), 3:(7500, 10000),
4:(10000,12500), 5:(12500,15000), 6:(15000,20000), 
7:(20000,25000), 8:(25000,30000), 9:(30000,35000),
10:(35000,40000), 11:(40000,50000), 12:(50000,60000),
13:(60000,75000), 14:(75000,100000), 15:(100000,150000),
16:(150000,1000000), -1:'decline', -2:'decline', -3:'decline'}

for line in infile:
    PERRP = line[117:119]
    '''
    RELATIONSHIP TO REFERENCE PERSON
    01	REFERENCE PERSON W/RELS.
    02	REFERENCE PERSON W/O RELS.
    03	SPOUSE
    04	CHILD
    05	GRANDCHILD
    06	PARENT
    07	BROTHER/SISTER
    08	OTHER REL. OR REF. PERSON
    09	FOSTER CHILD
    10	NONREL. OF REF. PERSON W/RELS.
    11	NOT USED
    12	NONREL. OF REF. PERSON W/O RELS.
    13	UNMARRIED PARTNER W/RELS.
    14	UNMARRIED PARTNER W/OUT RELS.
    15	HOUSEMATE/ROOMMATE W/RELS.
    16	HOUSEMATE/ROOMMATE W/OUT RELS.
    17	ROOMER/BOARDER W/RELS.
    18	ROOMER/BOARDER W/OUT RELS.
    '''
    # Only lines with code ' 1' or ' 2' are householders; other lines record other 
    # household members, and we don't want to count households multiple times.
    if PERRP in [' 1', ' 2']:
        ####
        # Age
        #####
        age = int(line[121:123])
        # Note this is top-coded; 85 could mean anything 85 and up
        '''
        Returns two characters representing age.
        00-79	Age in Years	
        80		80-84 Years Old
        85		85+ Years Old
        '''
        # Randomly "correct" for 80 and 85 topcoding
        if age==80:
            age = age + random.choice([0,0,0,0,0,1,1,1,1,2,2,2,3,3,4])
        if age == 85:
            age = age + random.choice([0]*10+[2]*8+[4]*6+[6]*4+[8]*2)
            
        ######
        # State 
        #####
        state = code_93_94[int(line[92:94])]
           
        #####
        # Household size
        #####
        household_size = int(line[58:60]) 
        
        #####
        #Income
        #####
        income_code = line[38:40]
        # Lookup code, report error to screen
        try:
            income = code_39_40[int(income_code)]
        except KeyError:
            print "income code ", income_code # report error to screen
        
        # Some income codes are 'declined', but the rest are 2-tuples specifying
        # the income in the interval (min, max).
        # Pick a multiple of $100 randomly in the interval.
        # Plotting a histogram as the midpoint of is incorrect because
        # the width should be shown as spread out across the full interval
        # to demontrate the tailed distribution.
        if type(income) == tuple:
            income = random.choice(range(income[0],income[1],100))
            if income < 0:
                income = "-$" + str(abs(income))
            else:
                income = "$" + str(income)
                
        ####
        # Print household to output file
        ####
        outfile1.write(str(age) + ", " + income + '\n')
        outfile2.write(state + ", " + str(household_size) + '\n')
infile.close()
outfile1.close()
outfile2.close() 