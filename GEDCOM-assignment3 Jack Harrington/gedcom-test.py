import datetime

""" 
@param          : fileName    - GEDCOM file to be parsed.
@return         : individuals - Nested dicitonaries of individuals listed in GEDCOM file.
@supported_tags : NAME, SEX, BIRTH, AGE, ALIVE, DEATH
"""
def parse_individuals_gedcom(fileName):
    # Computes current year for age calculation.
    current = datetime.datetime.now()
    current_year = current.year
    # Creates an empty dictionary of individuals.
    individuals = {}
    current_individual = None
    # Opens the file to be parsed.
    file = open(fileName, 'r', encoding='utf-8-sig')
    # Iterates through the lines in the file. 
    for line in file:
        line = line.strip()
        # Checks if line starts with an individual tag. 
        if line.startswith('0 @I'):
            individual_id = line.split('@')[1]
            # Creates an individual based on their ID from split. 
            individuals[individual_id] = {}
            current_individual = individual_id
        # Checks for name tag in line.
        if '1 NAME' in line:
            name = line.split('NAME')[1].strip()
            # Adds (key, value) for name.
            individuals[current_individual]['NAME'] = name
        # Checks for sex tag in line.
        if '1 SEX' in line:
            # Adds (key, value) for sex.
            individuals[current_individual]['SEX'] = line[6]
        # Checks for birth tag in line.
        if '1 BIRT' in line:
            line = file.readline()
            birth_date = line.split('DATE')[1].strip()
            individuals[current_individual]['BIRT'] = birth_date
            # If there is a birth_date, ALIVE set to 'True'.
            if birth_date:
                individuals[current_individual]['ALIVE'] = True
            # Calculates age based off of current year.
            individuals[current_individual]['AGE'] = int(current_year) - int(birth_date[6:])
        # Checks for death tag in line. 
        if line.startswith('1 DEAT'):
            line = file.readline()
            death_date = line.split('DATE')[1].strip()
            individuals[current_individual]['DEAT'] = death_date
            # If there is a death_date, ALIVE set to 'False'.
            if death_date:
                individuals[current_individual]['ALIVE'] = False
    # Returns the individuals
    return individuals

""" 
@param          : fileName    - GEDCOM file to be parsed.
@return         : families - Nested dicitonaries of individuals listed in GEDCOM file.
@supported_tags : FAM, MARR, DATE, DIV, HUSB, CHIL
"""
def parse_families_gedcom(fileName):
    families = {}
    children = []
    current_family = None
    file = open(fileName, 'r', encoding='utf-8-sig')
    for line in file:
        line = line.strip()
        if line.startswith('0 @F'):
            family_id = line.split('@')[1] 
            families[family_id] = {}
            current_family = family_id
            children = []
        if '1 MARR' in line:
            line = file.readline()
            married_date = line.split('DATE')[1].strip()
            families[current_family]['MARR'] = married_date
        if '1 DIV' in line:
            line = file.readline()
            divorced_date = line.split('DATE')[1].strip()
            families[current_family]['DIV'] = divorced_date
        if '1 HUSB' in line:
            husband_id = line.split('HUSB')[1].strip()
            # Adds (key, value) for husband.
            families[current_family]['HUSB'] = husband_id
        if '1 WIFE' in line:
            wife_id = line.split('WIFE')[1].strip()
            # Adds (key, value) for wife.
            families[current_family]['WIFE'] = wife_id
        if '1 CHIL' in line:
            children.append(line.split('CHIL')[1])
            # Adds (key, value) for child.
            families[current_family]['CHIL'] = children
    return families

""" 
@param          : d    - dictionary to be printed
@param          : indent - the indentation for nested dictionaries 
"""
def print_nested_dict(d, indent = 0):
    for key, value in d.items():
        print('\t' * indent + str(key) + ':')
        if isinstance(value, dict):
            print_nested_dict(value, indent)
            print('\n')
        else:
            print('\t' * (indent + 1) + str(value))

print('\nIndividual Data:\n')
print_nested_dict(parse_individuals_gedcom('GEDCOM-raw-data.ged'))

print('\nFamily Data:\n')
print_nested_dict(parse_families_gedcom('GEDCOM-raw-data.ged'))