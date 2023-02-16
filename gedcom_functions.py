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


         
