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
    for row in ind_matrix:
        if row[4] >= 17:
            for row in fam_matrix:
                if row[6] != "NA":
                    orphans.append(row[1]);
    return orphans

# List all couples who were married when the older spouse was
# more than twice as old as the younger spouse
def listLargeAgeDifferences(ind_matrix, fam_matrix):
    agediff = []
    for row in ind_matrix:
        if row[8] != "NA":
            partner_age = row[4]
            for i in fam_matrix:
                if row[8] != "NA":
                    if partner_age > 2 * row[4] or row[4] > 2 * partner_age:
                        agediff.append(row[1]);
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


# Vali
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




         
