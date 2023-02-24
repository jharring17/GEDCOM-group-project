# Tests for GEDCOM functions in gedcom_functions.py
import unittest
import gedcom_functions


class testGEDCOM(unittest.TestCase):

    # Should evaluate to True.
    def test1_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath('14 OCT 1912', '28 JUN 1961')
        self.assertTrue(result)

    # Should evaluate to True.
    def test2_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath('15 JUN 2005', '28 NOV 2020')
        self.assertTrue(result)

    # Should evaluate to True.
    def test3_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath('26 JAN 1945', '11 MAY 1989')
        self.assertTrue(result)

    # Should evaluate to False.
    def test4_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath('14 OCT 1912', '15 OCT 1800')
        self.assertFalse(result)

    # Should evaluate to False.
    def test5_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath('14 OCT 1912', '13 OCT 1912')
        self.assertFalse(result)

    # Should evaluate to True.
    def test1_birthBeforeMarriage(self):
        result = gedcom_functions.birthBeforeMarriage(["@F2@", "5 JUL 1945", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertTrue(result)

    # Should evaluate to True.
    def test2_birthBeforeMarriage(self):
        result = gedcom_functions.birthBeforeMarriage(["@F2@", "5 JUL 1945", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I7@", "Lori /Meumann/", "F", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertTrue(result)

    # Should evaluate to False.
    def test3_birthBeforeMarriage(self):
        result = gedcom_functions.birthBeforeMarriage(["@F2@", "5 JUL 1945", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I2@", "Brad /Meumann/", "M", "28 JUN 1961", "61", "True", "NA", "@F2@", "@F1@"])
        self.assertEqual(result, 'Error: Individual provided not in family.')

    # Should evaluate to False.
    def test4_birthBeforeMarriage(self):
        result = gedcom_functions.birthBeforeMarriage(["@F2@", "5 JUL 1945", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I3@", "Sally /Go/", "F", "8 FEB 1961", "62", "True", "NA", "@F3@", "@F1@"])
        self.assertEqual(result, 'Error: Individual provided not in family.')

    # Should evaluate to False.
    def test5_birthBeforeMarriage(self):
        result = gedcom_functions.birthBeforeMarriage(["@F2@", "5 JUL 1945", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I14@", "Jack", "M", "6 JAN 1968", "55", "True", "3 JAN 1999", "NA", "@F5@"])
        self.assertEqual(result, 'Error: Individual provided not in family.')
    
    def test1_listLargeAgeDifferences(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLargeAgeDifferences(i_mat, f_mat)
        self.assertEqual(result, ['@F2@'])

    def test2_listLargeAgeDifferences(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat = [['@F1@', '18 Jan 2010', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLargeAgeDifferences(i_mat, f_mat)
        self.assertEqual(result, ['@F1@', '@F2@'])

    def test3_listLargeAgeDifferences(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat = [['@F1@', '18 Jan 2100', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 2200', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLargeAgeDifferences(i_mat, f_mat)
        self.assertEqual(result, [])

    def test4_listLargeAgeDifferences(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'F7'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F7@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat = [['@F1@', '18 Jan 2100', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 2200', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2000', 'NA', '@I5@', 'David Lee', '@I9@', 'Linda Chen', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLargeAgeDifferences(i_mat, f_mat)
        self.assertEqual(result, ['@F7@'])

    def test5_listLargeAgeDifferences(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'F7'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F7@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1990', 60, True, 'NA', '@F3@', '@F4@']]

        f_mat = [['@F1@', '18 Jan 2010', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 2200', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2000', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I10@', 'Stephanie Wong', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2000', 'NA', '@I5@', 'David Lee', '@I9@', 'Linda Chen', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLargeAgeDifferences(i_mat, f_mat)
        self.assertEqual(result, ['@F1@', '@F4@', '@F7@'])


    # Should evaluate to True.
    def test1_listOrphans(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 17, True, 'NA', 'NA', '@F4@']]

        f_mat = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'David Lee', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listOrphans(i_mat, f_mat)
        self.assertEqual(result, ['David Lee', 'Stephanie Wong'])


    def test2_listOrphans(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        f_mat = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'David Lee', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listOrphans(i_mat, f_mat)
        self.assertEqual(result, [])

    def test3_listOrphans(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 17, True, 'NA', 'NA', '@F4@']]

        f_mat = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'David Lee', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listOrphans(i_mat, f_mat)
        self.assertEqual(result, ['David Lee', 'Stephanie Wong'])

    def test4_listOrphans(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 12, True, 'NA', '@F4@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 17, True, 'NA', 'NA', '@F4@']]

        f_mat = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'David Lee', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listOrphans(i_mat, f_mat)
        self.assertEqual(result, ['John Smith', 'David Lee', 'Stephanie Wong'])

    def test5_listOrphans(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        f_mat = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'David Lee', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listOrphans(i_mat, f_mat)
        self.assertEqual(result, [])

    # Should evaluate to True.
    def test1_listDeceased(self):
        individual_matrix1 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]
        result = gedcom_functions.listDeceased(individual_matrix1)
        self.assertEqual(result, ['Bob Johnson', 'Karen Lee'])

    # Should evaluate to True.
    def test2_listDeceased(self):
        individual_matrix2 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, False, '05 Oct 2020', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]
        result = gedcom_functions.listDeceased(individual_matrix2)
        self.assertEqual(result, ['Bob Johnson', 'Mike Johnson', 'Karen Lee'])

    # Should evaluate to True.
    def test3_listDeceased(self):
        individual_matrix3 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, True, 'NA', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]
        result = gedcom_functions.listDeceased(individual_matrix3)
        self.assertEqual(result, ['Bob Johnson'])

    # Should evaluate to True.
    def test4_listDeceased(self):
        individual_matrix4 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, True, 'NA', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, True, 'NA', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]
        result = gedcom_functions.listDeceased(individual_matrix4)
        self.assertEqual(result, [])

    # Should evaluate to True.
    def test5_listDeceased(self):
        individual_matrix5 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, False, '05 Jan 2022', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, False, '05 Jan 2022', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F1@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, False, '05 Jan 2022', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, False, '05 Jan 2022', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, False, '05 Jan 2022', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, False, '05 Jan 2022', 'NA', '@F2@']]
        result = gedcom_functions.listDeceased(individual_matrix5)
        self.assertEqual(result, ['John Smith', 'Jane Doe', 'Bob Johnson', 'Mary Brown', 'David Lee', 'Samantha Kim', 'Mike Johnson', 'Karen Lee', 'Eric Chang', 'Stephanie Wong'])

    # Should evaluate to True.
    def test1_listLivingSingle(self):
        individual_matrix6 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        family_matrix1 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'David Lee', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingSingle(individual_matrix6, family_matrix1)
        self.assertEqual(result, ['John Smith', 'Mary Brown', 'Mike Johnson', 'Eric Chang'])

    # Should evaluate to True.
    def test2_listLivingSingle(self):
        individual_matrix7 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        family_matrix2 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingSingle(individual_matrix7, family_matrix2)
        self.assertEqual(result, ['John Smith', 'Mike Johnson', 'Eric Chang'])

    # Should evaluate to True.
    def test3_listLivingSingle(self):
        individual_matrix8 =[['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        family_matrix3 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'John Smith', '@I11@', 'Person Name', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingSingle(individual_matrix8, family_matrix3)
        self.assertEqual(result, [])

    # Should evaluate to True.
    def test4_listLivingSingle(self):
        individual_matrix9 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        family_matrix4 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingSingle(individual_matrix9, family_matrix4)
        self.assertEqual(result, ['Mike Johnson', 'Eric Chang'])

    # Should evaluate to True.
    def test5_listLivingSingle(self):
        individual_matrix10 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, True, 'NA', 'NA', 'NA']]

        family_matrix5 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingSingle(individual_matrix10, family_matrix5)
        self.assertEqual(result, ['Mike Johnson', 'Eric Chang', 'Stephanie Wong'])


    # Should evaluate to True.
    def test1_listLivingMarried(self):
        ind_m = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, True, 'NA', 'NA', 'NA']]

        fam_m = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingMarried(ind_m, fam_m)
        self.assertEqual(result, ['Jane Doe'])

    def test2_listLivingMarried(self):
        ind_m = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Jack Dance', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F1@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, True, 'NA', 'NA', 'NA']]

        fam_m = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingMarried(ind_m, fam_m)
        self.assertEqual(result, ['Jane Doe', 'Jack Dance'])


    def test3listLivingMarried(self):
        ind_m = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Daniel Kim', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Andrew Kim', 'Female', '06 Feb 1975', 48, True, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Jack Dance', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F1@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, True, 'NA', 'NA', 'NA']]

        fam_m = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingMarried(ind_m, fam_m)
        self.assertEqual(result, ['Jane Doe', 'Jack Dance', 'Daniel Kim', 'Andrew Kim' ])

    def test4listLivingMarried(self):
        ind_m = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Daniel Kim', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Andrew Kim', 'Female', '06 Feb 1975', 48, True, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Jack Dance', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F1@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, True, 'NA', 'NA', 'NA']]

        fam_m = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', 'NA', '@I8@', 'Stephanie Wong', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingMarried(ind_m, fam_m)
        self.assertEqual(result, ['Jane Doe', 'Jack Dance', 'Daniel Kim', 'Stephanie Wong', 'Andrew Kim' ])


    def test5listLivingMarried(self):
        ind_m = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, False, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, False, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Daniel Kim', 'Male', '29 Apr 1998', 23, False, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, False, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, False, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Andrew Kim', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Jack Dance', 'Male', '27 Nov 1989', 32, False, 'NA', '@F5@', '@F1@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, False, 'NA', 'NA', 'NA']]

        fam_m = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.listLivingMarried(ind_m, fam_m)
        self.assertEqual(result, [])


    # Should evaluate to True.
    def test1_marriageBeforeDivorce(self):
        result = gedcom_functions.marriageBeforeDivorce(["@F2@", "5 JUL 1945", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertTrue(result)

        # Should evaluate to False.
    def test2_marriageBeforeDivorce(self):
        result = gedcom_functions.marriageBeforeDivorce(["@F2@", "5 JUL 1945", "5 JUL 1945", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertFalse(result)
       
    # Should evaluate to True.
    def test3_marriageBeforeDivorce(self):
        result = gedcom_functions.marriageBeforeDivorce(["@F2@", "5 JUL 1945", "5 JUL 1946", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertTrue(result)

        # Should evaluate to False.
    def test4_marriageBeforeDivorce(self):
        result = gedcom_functions.marriageBeforeDivorce(["@F2@", "5 JUL 1945", "5 JUL 1944", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertFalse(result)

        # Should evaluate to True.
    def test5_marriageBeforeDivorce(self):
        result = gedcom_functions.marriageBeforeDivorce(["@F2@", "5 JUL 1945", "5 JUL 2000", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertTrue(result)

        # Should evaluate to True.
    def test1_marriageBeforeDeath(self):
        result = gedcom_functions.marriageBeforeDeath(["@F2@", "5 JUL 1945", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertTrue(result)

        # Should evaluate to True.
    def test2_marriageBeforeDeath(self):
        result = gedcom_functions.marriageBeforeDeath(["@F2@", "5 JUL 1946", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertTrue(result)

        # Should evaluate to False.
    def test3_marriageBeforeDeath(self):
        result = gedcom_functions.marriageBeforeDeath(["@F2@", "5 JUL 2000", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertFalse(result)

        # Should evaluate to False.
    def test4_marriageBeforeDeath(self):
        result = gedcom_functions.marriageBeforeDeath(["@F2@", "5 JUL 2001", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertFalse(result)

        # Should evaluate to False.
    def test5_marriageBeforeDeath(self):
        result = gedcom_functions.marriageBeforeDeath(["@F2@", "5 JUL 2002", "NA", "@I6@",  "Arthur /Meumann/", "@I7@", "Lori /Meumann/",['@I2@', '@I8@']], ["@I6@", "Arthur /Meumann/", "M", "6 DEC 1922", "101", "False", "3 JAN 1999", "NA", "@F5@"])
        self.assertFalse(result)  


# Enables us to call test file like python file.
if __name__ == '__main__':
    unittest.main()
