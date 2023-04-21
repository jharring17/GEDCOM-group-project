# GEDCOM Functions to data validity.
from datetime import *
from dateutil import parser

# Validates if birth comes before death.
def birthBeforeDeath(birth, death):
    birth_date = parser.parse(birth)
    death_date = parser.parse(death)
    if (death_date < birth_date):
        # If death before birth.
        return False
    else:
        # If death after birth.
        return True

# Validates that a person was born before they were married.
def birthBeforeMarriage(family, individual):
    partnerOneID = family[3]
    partnerTwoID = family[5]
    individualID = individual[0]
    # Preforms check to see if family member is spouse.
    if ((partnerOneID == individualID) or (partnerTwoID == individualID)):
        # Parses birth_date and marriage_date.
        marriage_date = parser.parse(family[1])
        birth_date = parser.parse(individual[3])
        # Checks that marriage_date occurs after birth_date.
        if (marriage_date > birth_date):
            return True
        else:
            return False
    else:
        return 'Error: Individual provided not in family.'

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

# Lists all people who: 
    # living
    # over 30
    # never married
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

# no parents should be married to any of their descendants
# should return true if none are married to descendants
# check if children id matches spouse id
# then check if they have children
# do this until we reach the "leaf" or last child without children
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

# Fewer than 15 siblings
# Returns True if family has less than 15 siblings
# Returns False if family has 15 or more siblings
def sibling15(fam_matrix):
    for row in fam_matrix:
        if (row[7]!= 'NA') and (len(row[7]) >= 15):
            return False
    return True

# Siblings should not marry
# Returns true if no siblings are married to eachother
# Returns false if sibling is married to another sibling
def marriedSiblings(fam_matrix):
    for row in fam_matrix:
        if row[7] != 'NA':
            siblings = row[7]
            if len(siblings) >= 2:
                for rower in fam_matrix:
                    hus = rower[3]
                    wife = rower[5]
                    if (hus in siblings) and (wife in siblings):
                        return False
    return True

# List Multiple Births
# List all multiple births in a GEDCOM file
# Multiple births - siblings born on same day
# Returns a list of lists where each sublist is siblings born on the same day
def listMulBirt(ind_matrix, fam_matrix):
    family_bdays = {}
    for fam in fam_matrix:
        if fam[7] != 'NA':
            fam_id = fam[0]
            siblings = fam[7]
            family_bdays[fam_id] = {}
            for sib in siblings:
                for person in ind_matrix:
                    if person[0] == sib:
                        bday = person[3]
                        if bday not in family_bdays[fam_id]:
                            family_bdays[fam_id][bday] = [sib]
                        else:
                            family_bdays[fam_id][bday].append(sib)
    res = []
    for fam_id, bdays in family_bdays.items():
        for bday in bdays:
            mems = bdays[bday]
            if len(mems) > 1:
                res.append(mems)
    return res 


# Multiple Births <= 5
# No more than five siblings should be born at the same time
# Multiple births - siblings born on same day
# Returns false if over 5 multiple births, true if otherwise
def less5Birt(ind_matrix, fam_matrix):
    for row in fam_matrix:
        siblings = row[7]
        if row[7] != 'NA' and len(siblings) > 5:
            birth_arr = [None] * len(siblings)
            date_index = 0
            for element in siblings:
                for rower in ind_matrix:
                    if element == rower[0]:
                        birth_arr[date_index] = rower[3]
                date_index += 1
            counter = {}
            for birthday in birth_arr:
                if birthday in counter:
                    counter[birthday] += 1
                else:
                    counter[birthday] = 1
            for item, count in counter.items():
                if count > 5:
                    return False
    return True

# Validates that a person was married before divorce
def marriageBeforeDivorce(family, individual):
    partnerOneID = family[3]
    partnerTwoID = family[5]
    individualID = individual[0]
    if ((partnerOneID == individualID) or (partnerTwoID == individualID)):
        if (family[2]) != "NA":
            marriage_date = parser.parse(family[1])
            divorce_date = parser.parse(family[2])
            if (marriage_date < divorce_date):
                return True
            else:
                return False
        else: return True
    else:
        return 'Error: Individual provided not in family.'

# Validates that a person was married before their death.
def marriageBeforeDeath(family, individual):
    partnerOneID = family[3]
    partnerTwoID = family[5]
    individualID = individual[0]
    if ((partnerOneID == individualID) or (partnerTwoID == individualID)):
        marriage_date = parser.parse(family[1])
        death_date = parser.parse(individual[6])
        if (marriage_date < death_date):
            return True
        else:
            return False
    else:
        return 'Error: Individual provided not in family.'
         
