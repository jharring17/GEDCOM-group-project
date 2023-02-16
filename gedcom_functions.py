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

