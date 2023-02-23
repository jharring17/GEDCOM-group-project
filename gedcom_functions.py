# GEDCOM Functions to data validity.
from datetime import *
from dateutil import parser

#TODO: Replace input with a matrix.
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
    for row in ind_matrix:
        if row[4] >= 30 and row[8] == "NA":
            single.append(row[1]);
    return single

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
         
# Checks if anyone has an age of over 150yrs and is alive.
def olderThan150(individuals):
    # Iterates the individuals.
    for row in individuals:
        # Checks if their age attribute is > 150.
        person = row[1]
        if row[4] > 150 and row[5] == True:
            return("Error: " + person + " should not be listed as alive.")