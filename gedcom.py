#########################################################################################################################
# Title         : gedcom.py                                                                                             #
# Author        : Jack Harrington                                                                                       #
# Version       : 1.0                                                                                                   #
# Pledge        : I pledge my honor that I have abided by the Stevens Honor System.                                     #
# Description   : Python file that extracts data from a GEDCOM file, reformats the line inputs, and checks formatting.  #
#########################################################################################################################

# Encoding must be added to remove the beginning and ending file tags. 
gedcom_file = open('GEDCOM-Jack-Harrington.ged', 'r', encoding='utf-8-sig')

# Loops through all lines in gedcom_file.
while True:
    # Reads lines from the gedcom_file and prints.
    line = gedcom_file.readline()
    
    # Preforms a check to see if the line in the file is empty. 
    if not line:
        break
    
    # Clears the lines of unnecessary appended spaces or '\n' characters.
    line = line.strip()
    
    # Prints line in required formatting. 
    print("--> " + line)

    # Takes and removes level from string.
    level, rest = line.split(" ", 1)

    # Strips the rest of the string.
    rest = rest.strip()

    # Checks if there is a space in the string.
    if ' ' in rest:
        # If there is a space, split into tag and args.
        tag, args = rest.split(" ", 1)
    else:
        # Else, tag assumes value of rest and args remain empty.
        tag, args = (rest, "")

    # Valids tags from the "project overview."
    valid_tags = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "NOTE", "DATE"}

    tag = tag.strip()
    # Checks if the tag from the string is valid.
    if tag in valid_tags:
        # If valid, option becomes 'Y' for yes.
        option_symbol = 'Y'
    else:
        # If invalid, option becomes 'N' for no.
        option_symbol = 'N'

    # Removes support for 1 DATE. 
    if level == "1" and tag == "DATE":
        option_symbol = 'N'

    # Removes support for 2 NAME.
    if level == "2" and tag == "NAME":
        option_symbol = 'N'

    # Adds support for INDI and FAM as third token.
    if args == "INDI" or args == "FAM":
        option_symbol = 'Y'

    # Prints the GEDCOM arguments with option_symbol.
    print(f"<--{level}|{tag}|{option_symbol}|{args}")

# Closes the gedcom_file. 
gedcom_file.close()