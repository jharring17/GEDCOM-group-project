# File that parses GEDCOM files.

from tabulate import tabulate
from gedcom_functions import *

filename = "./data/newfam.ged"

#TODO: Change this from static matrix to expanding.
individual = [[0 for j in range(9)] for i in range(34)]
family = [[0 for j in range(8)] for i in range(9)]

row = -1
famrow = -1
dead = False
marriage = 1 #1 false, 2 true, 3 divorced

with open(filename, "r") as gedcomFile:

    #grabbing all of our data
    for myline in gedcomFile:
        line = myline.strip('\n')
        level = line[0]
        words = line.split()
        last = words[-1]

        if last == 'FAM' or last == 'INDI':
            tag = words[-1]
            arg = words[1:-1]
            arg = " ".join(arg)
        
        elif level == '0' and line[2:6] != 'HEAD' and line[2:6] != 'TRLR' and line[2:6] != 'NOTE':            
            tag = words[-1]
            arg = words[1:]
            arg = " ".join(arg)
        else:
            tag = words[1]
            arg = words[2:]
            arg = " ".join(arg)

        taglist0 = ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE']
        taglist1 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
        taglist2 = ['DATE']
        taglist4 = ['INDI', 'FAM']
        match = False

        if level == "0":
            if tag in taglist0:
                match = True

        elif level == "1":
            if tag in taglist1:
                match = True

        elif level == "2":
            if tag in taglist2:
                match = True

        if match == True:
            valid = 'Y'
        else:
            valid = 'N'


##################################checking individual data

        if level == "0" and tag in taglist4:
            row += 1
            
        if tag == "INDI":
            individual[row][0] = arg

        elif tag == "NAME":
            individual[row][1] = arg

        elif tag == "SEX":
            individual[row][2] = arg

        elif tag == "BIRT":
            dead = False
            marriage = 1

        elif tag == "DEAT":
            dead = True
            marriage = 1

        elif tag == "DATE":
            if marriage == 1:
                if dead == False:
                    individual[row][3] = arg
                    individual[row][6] = "NA"
                else:
                    individual[row][6] = arg
            elif marriage == 2:
                family[famrow][1] = arg
            else:
                family[famrow][2] = arg

                
        elif tag == "FAMS":
            individual[row][8] = arg
            

        elif tag == "FAMC":
            individual[row][7] = arg


        #######fam data stuff
        elif tag == "FAM":
            famrow += 1
            family[famrow][0] = arg

        elif tag == "MARR":
            marriage = 2
            
        elif tag == "HUSB":
            family[famrow][3] = arg
            for b in individual:
                if b[0] == arg:
                    family[famrow][4] = b[1]

        elif tag == "WIFE":
            family[famrow][5] = arg
            for c in individual:
                if c[0] == arg:
                    family[famrow][6] = c[1]

        elif tag == "CHIL":
            arglist = [arg]
            if type(family[famrow][7]) is list:
                family[famrow][7].append(arg)
            else:
                family[famrow][7] = arglist
                               
        elif tag == "DIV":
            marriage = 3

        if family[famrow][1] == 0:
            family[famrow][1] = "NA"
        if family[famrow][2] == 0:
            family[famrow][2] = "NA"
        

        if individual[row][7] == 0:
            individual[row][7] = "NA"

        if individual[row][8] == 0:
            individual[row][8] = "NA"

            
        ##calculate and record if alive
        alive = True
        died = individual[row][6]
        if died == 'NA':
            alive = True
        else:
            alive = False
            
        individual[row][5] = alive

   # print('--> ' + line)
    #print('<-- ' + level + '|' + tag + '|' + valid + '|' + arg)

    ############################################
        ##calculating dates
    months = {
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "MAY": 5,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12,
        }

        ##calculate and record age
    current_day = 9
    current_month = 2
    current_year = 2023

    rownum = 0
    
    for x in individual:
        if individual[rownum][3] == 0:
            break
        
        birthday = individual[rownum][3]
  
        day, month, year = birthday.split()

        
       
        day = int(day)
        month = months[month]
        year = int(year)

        year = current_year - year

        if month >= current_month and day > current_day:
            age = year - 1
        else:
            age = year
        
        individual[rownum][4] = age
        rownum += 1

#############################################################
    counter = 0
    for person in individual:
        if (person[0] != 0):
            counter +=1
    individual = individual[:counter]

    #fam stuff:
    count = 0
    for a in individual:
        if a[8] != "NA":
            family[count][0] = a[8]

    #print individual data
    indvheaders = ['ID', 'NAME', 'GENDER', 'BIRTHDAY', 'AGE', 'ALIVE', 'DEATH', 'CHILD', 'SPOUSE']
    indtable = [indvheaders] + individual

    print(tabulate(individual, headers=indvheaders, tablefmt='fancy_grid'))

    #print family data
    famheaders = ['ID', 'MARRIED', 'DIVORCED', 'HUSBAND ID', 'HUSBAND NAME', 'WIFE ID', 'WIFE NAME', 'CHILDREN']
    famtable = [famheaders] + family

    print(tabulate(family, headers=famheaders, tablefmt='fancy_grid'))

##############################################################
# Tests the functions with the data.
print("\nTesting functions on the data: ") 

# Checks that each of the individuals who are dead were living first.
for i in individual:
    if (i[6] == 'NA' or i[6] == 0):
        pass
    else:
        result = birthBeforeDeath(i[3], i[6])
        result = str(result)
        print(i[1] + " was born and then died: " + result)

# Checks that married individuals were born before they were married.
for i in individual:
    for f in family:
        if (birthBeforeMarriage(i, f) == None or birthBeforeMarriage(i, f) == 'Error: Individual provided not in family.'):
            pass
        else:
            print(birthBeforeMarriage(i, f))

if (listLargeAgeDifferences(individual, family) == []):
    print("There are no large age differences in the dataset.")
else:
    print(listLargeAgeDifferences(individual, family))

livingSingle = []
for person in individual:
    if person[8] == 'NA':
        livingSingle.append(person[1])
print(livingSingle)
print(listDeceased(individual))









            
