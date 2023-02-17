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
def listOrphans(children):
    orphans = []
    for i in children: 
        age = parser.parse(children[i].age)
        #Child is not orphan if greater than 17 years of age
        if (age > 17):
            continue
        else:
            #Check if both parents are dead
            if (((children[i].parent1.dead) and (children[i].parent2.dead)) != True):
                continue
            #Append to orphan list
            orphans += children[i]
    return orphans

# List all couples who were married when the older spouse was
# more than twice as old as the younger spouse
def listLargeAgeDifferences(couples):
    ageDiff = []
    for i in couples: 
        # Use marriage date - birth date to figure out ages of the spouses
        # For simplicity use marriage year and birth year
        marriage = parser.parse(couples[i].marriageDate)
        spouse1_birth = parser.parse(couples[i].spouse1.birth)
        spouse2_birth = parser.parse(couples[i].spouse.birth)
        # AAM = Age at Marriage
        spouse1_AAM = marriage - spouse1_birth
        spouse2_AAM = marriage - spouse2_birth

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





         
