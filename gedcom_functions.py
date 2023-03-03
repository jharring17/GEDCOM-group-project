# GEDCOM Functions to data validity.
from datetime import *
from dateutil import parser

# Validates if birth comes before death.
def birthBeforeDeath(individuals):
    result_array = []
    for row in individuals:
        if (row[6] == 'NA'):
            pass
        else:
            individual = row[1]
            birth_date = parser.parse(row[3])
            death_date = parser.parse(row[6]) 
            if (death_date < birth_date):
                result_array.append("Error: " + individual + " died before they were born.")
    return result_array

# Validates that a person was born before they were married.
def birthBeforeMarriage(family, individual):
    result_array = []
    for i in individual:
        individual_id = i[0]
        individual_name = i[1]
        individual_birth = parser.parse(i[3])
        for j in family:
            if individual_id == j[3] or individual_id == j[5]:
                marriage_date = parser.parse(j[1])
                if individual_birth > marriage_date:
                    result_array.append("Error: " + individual_name + " was married before they were born.")
    return result_array

# Lists all orphaned children when passed
# a list of children (under 18).
def listOrphans(ind_matrix, fam_matrix):
    orphans = []
    dad = 0
    mom = 0
    mom_dead = False
    dad_dead = False
    for row in ind_matrix:
        if row[4] < 18:
            fam_id = str(row[7])
            for r in fam_matrix:
                if fam_id == r[0]:
                    dad = r[3]
                    mom = r[5]
                    dad_dead = False
                    mom_dead = False
            for rower in ind_matrix:
                if rower[0] == dad:
                    if rower[5] == False:
                        dad_dead = True
                elif rower[0] == mom:
                    if rower[5] == False:
                        mom_dead = True
            if mom_dead == True and dad_dead == True:
                orphans.append(row[1]);
    return orphans

# List all couples who were married when the older spouse was
# more than twice as old as the younger spouse
# married
# older spouse more than twice as old as younger spouse at marriage
def listLargeAgeDifferences(ind_matrix, fam_matrix):
    agediff = []
    for row in fam_matrix:
        hus_birt = ''
        wife_birt = ''
        marry_date = row[1]
        hus_name = row[4]
        wife_name = row[6]

        for rower in ind_matrix:
            if wife_name == rower[1]:
                wife_birt = datetime.strptime(rower[3], '%d %b %Y')
            elif hus_name == rower[1]:
                hus_birt = datetime.strptime(rower[3], '%d %b %Y')

        if hus_birt != '' and wife_birt != '':
            marry_date_good = datetime.strptime(marry_date, '%d %b %Y')
            hus_age = (marry_date_good - hus_birt).days // 365
            wife_age = (marry_date_good - wife_birt).days // 365
            
            if hus_age > (wife_age * 2) or wife_age > (hus_age * 2):
                agediff.append(row[0])
                
    return agediff
        
# Lists all deceased individuals
def listDeceased(ind_matrix):
    deceased = []
    for row in ind_matrix:
        if row[6] != "NA":
            deceased.append(row[1])
    return deceased

# Lists all people over 30 who have never been married
def listLivingSingle(ind_matrix, fam_matrix):
    single = []
    there = False
    for row in ind_matrix:
        if row[4] >= 30 and row[5] == True:
            for r in fam_matrix:
                if r[4] == row[1] or r[6] == row[1]:
                    there = True
            if there == False:
                single.append(row[1])
    return single

def noMarDes(ind_matrix, fam_matrix):
    for row in fam_matrix:
        husband = row[3]
        wife = row[5]
        if row[7] != 'NA':
            children = row[7]
            des = listDes(ind_matrix, fam_matrix, children)
            for person in des:
                for r in fam_matrix:
                    if (r[3] == husband and r[5] == person) or (r[3] == person and r[5] == wife):
                        return False
    return True
    
#lists all living and married (does not include divorced)
def listLivingMarried(ind_matrix, fam_matrix):
    married = []
    for row in fam_matrix:
        if row[2] == 'NA':
            for r in ind_matrix:
                if row[4] == r[1] or row[6] == r[1]:
                    if r[5] == True:
                        married.append(r[1])
    return married

# noMarDes helper function
# lists descendants of a parent
def listDes(ind_matrix, fam_matrix, childList):
    des = childList

    for child in childList:
        for rower in fam_matrix:
            if (child == rower[3] or child == rower[5]) and rower[7] != 'NA':
                children = rower[7]
                des.append(listDes(ind_matrix, fam_matrix, children))
                des = flatten(des)
    return des

# flattens list [hi, hello, [here]] -> [hi, hello, here]
def flatten(lis):
    res = []
    for item in lis:
        if isinstance(item, list):
            res.extend(flatten(item))
        else:
            res.append(item)
    return res

# Validates that a person was married before divorce
def marriageBeforeDivorce(fam_matrix, ind_matrix):
    arr = []
    for row in ind_matrix:
        fam_id = row[8]
        ind_name = row[1]
        for rowr in fam_matrix:
            if rowr[0] == fam_id:
                if rowr[2] != "NA":
                    marriage_date = parser.parse(rowr[1])
                    divorce_date = parser.parse(rowr[2])
                    if (marriage_date < divorce_date):
                        continue
                    else:
                        arr.append("Error: " + ind_name + " was divorced before they were married.")
                else:
                    continue
    return arr
    
# Validates that a person was married before their death.
def marriageBeforeDeath(fam_matrix, ind_matrix):
    arr = []
    for row in ind_matrix:
        fam_id = row[8]
        ind_name = row[1]
        if row[6] != "NA" :
            death_date = parser.parse(row[6])
            for rowr in fam_matrix:
                if rowr[0] == fam_id:
                    marriage_date = parser.parse(rowr[1])
                    if (marriage_date < death_date):
                        continue
                    else:
                        arr.append("Error: " + ind_name + " died before they were married.")
                else:
                    continue
    return arr
    
# Checks if anyone has an age of over 150yrs and is alive.
def olderThan150(individuals):
    result_array = []
    # Iterates the individuals.
    for row in individuals:
        # Checks if their age attribute is > 150.
        person = row[1]
        if row[4] > 150 and row[5] == True:
            result_array.append("Error: " + person + " should not be listed as alive.")
    return result_array

# All male members of a family should have the same last name.
def maleLastNames(individual, family):
    result_array = []
    # Iterate the family matrix.
    for i in family:
        father_name = i[4]
        father_name = father_name.split(" ")[1]
        # Checks if the family does not have children.
        if i[7] == 'NA':
            pass
        # If the family has children.
        else:
            children = i[7]
            # Iterate the children in the family matrix.
            for child in children:
                # Iterate the individual matrix.
                for person in individual:
                    # Check if the child is the correct person and is male.
                    if person[0] == child and person[2] == 'M':
                        child_name = person[1].split(" ")[1]
                        # Check if child's last name is equal to their father's.
                        if (child_name != father_name):
                            result_array.append("Error: " + person[0] + " does not have the same name as their father.")
                    else:
                        pass
    return result_array

# List all living spouses and descendants of
# people in a GEDCOM file who died in the last 30 days
def listRecentSurvivors(ind_matrix, fam_matrix):
    living_survivors = []
    for row in ind_matrix:
        if row[6] != 'NA':
            person_ID = row[0]
            death_day = datetime.strptime(row[6], '%d %b %Y')
            current_datetime = datetime.now()
            days_since_death = (current_datetime - death_day).days
            if days_since_death < 31 :
                for r in fam_matrix:
                    # Get spouse ID
                    if person_ID == r[3]:
                        living_survivors.append(r[5])
                        if r[7] != 0:
                            for c in r[7]:
                                living_survivors.append(c)
                    elif person_ID == r[5]:
                        living_survivors.append(r[3])
                        if r[7] != 0:
                            for c in r[7]:
                                living_survivors.append(c)
                    #Iterate through children and get IDs
             
    return living_survivors

# List all people in a GEDCOM file who were born in the last 30 days
def listRecentBirths(ind_matrix):
    new_births = []
    for row in ind_matrix:
        if row[5] == True:
            birth = datetime.strptime(row[3], '%d %b %Y')
            current_datetime = datetime.now()
            days_since_birth = (current_datetime - birth).days
            # Not 100% sure if this is how you check the last 30 days
            if days_since_birth < 31:
                new_births.append(row)
    return new_births

def divorceBeforeDeath(fam_matrix, ind_matrix):
    arr = []
    for row in ind_matrix:
        fam_id = row[8]
        ind_name = row[1]
        if (row[6] != "NA"):
            death_date = parser.parse(row[6])
            for rowr in fam_matrix:
                if rowr[0] == fam_id:
                    if (rowr[2])!= "NA":
                        divorce_date = parser.parse(rowr[2])
                        if (divorce_date < death_date):
                            continue
                        else:
                            arr.append("Error: " + ind_name + " died before their divorce.")
                    else:
                        continue
    return arr
    
def birthBeforeMP(fam_matrix, ind_matrix):
    arr=[]
    for row in ind_matrix:
        ind_id = row[0]
        ind_name = row[1]
        birth_date = parser.parse(row[3])
        for rowr in fam_matrix:
            if ind_id in rowr[7]:
                marriage_date = parser.parse(rowr[1])
                if (marriage_date < birth_date):
                    continue
                else:
                    arr.append(ind_name + " was born before their parents were married.")
    return arr