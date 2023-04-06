# Tests for GEDCOM functions in gedcom_functions.py
import unittest
import gedcom_functions

class testGEDCOM(unittest.TestCase):

    def test1_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath([['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 3000', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']])
        self.assertEqual(result, ["Error: Robert Johnson died before they were born."])

    def test2_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath([['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']])
        self.assertEqual(result, [])

    def test3_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath([['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 2023', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']])
        self.assertEqual(result, ["Error: Bob Johnson died before they were born."])

    def test4_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath([['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@']])
        self.assertEqual(result, [])

    def test5_birthBeforeDeath(self):
        result = gedcom_functions.birthBeforeDeath([['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']])
        self.assertEqual(result, [])

    def test1_birthBeforeMarriage(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@']]
        f_mat = [['@F1@', '18 Jan 2000', 'NA', '@I1@', 'John Smith', '@I11@', 'Jane Doe', 'NA']]
        result = gedcom_functions.birthBeforeMarriage(f_mat, i_mat)
        self.assertEqual(result, [])

    def test2_birthBeforeMarriage(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I12@', 'Joseph Barry', 'Male', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@']]
        f_mat = [['@F1@', '18 Jan 1800', 'NA', '@I1@', 'John Smith', '@I11@', 'Jane Doe', 'NA']]
        result = gedcom_functions.birthBeforeMarriage(f_mat, i_mat)
        self.assertEqual(result, ['Error: John Smith was married before they were born.', 'Error: Jane Doe was married before they were born.'])

    def test3_birthBeforeMarriage(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@']]  
        f_mat = [['@F1@', '18 Jan 1800', 'NA', '@I1@', 'John Smith', '@I11@', 'Jane Doe', 'NA']]
        result = gedcom_functions.birthBeforeMarriage(f_mat, i_mat)
        self.assertEqual(result, ['Error: John Smith was married before they were born.', 'Error: Jane Doe was married before they were born.'])

    def test4_birthBeforeMarriage(self):
        i_mat = [] 
        f_mat = []
        result = gedcom_functions.birthBeforeMarriage(f_mat, i_mat)
        self.assertEqual(result, [])

    def test5_birthBeforeMarriage(self):
        i_mat = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@']]
        f_mat = []
        result = gedcom_functions.birthBeforeMarriage(f_mat, i_mat)
        self.assertEqual(result, [])
    
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

    def test1noMarDes(self):
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
        
        result = gedcom_functions.noMarDes(ind_m, fam_m)
        self.assertTrue(result)

    def test2noMarDes(self):
        ind_m = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, False, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, False, 'NA', 'NA', 'I9'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@I10'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Daniel Kim', 'Male', '29 Apr 1998', 23, False, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, False, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, False, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Andrew Kim', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Jack Dance', 'Male', '27 Nov 1989', 32, False, 'NA', '@F5@', '@F1@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, False, 'NA', 'NA', 'NA']]

        fam_m = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', '@I10@'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I7@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@I11@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', ['@I2@', '@I3@', '@I4@']],
        ['@F10@', '30 Oct 2010', 'NA', '@I9@', 'Eric Chen', '@I2@', 'Jane Doe', 'NA']]

        result = gedcom_functions.noMarDes(ind_m, fam_m)
        self.assertFalse(result)

    def test3noMarDes(self):
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
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', ['@I2@']],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.noMarDes(ind_m, fam_m)
        self.assertTrue(result)

    def test4noMarDes(self):
        ind_m = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, False, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, False, 'NA', 'NA', 'I9'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@I10'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Daniel Kim', 'Male', '29 Apr 1998', 23, False, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, False, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, False, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Andrew Kim', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Jack Dance', 'Male', '27 Nov 1989', 32, False, 'NA', '@F5@', '@F1@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, False, 'NA', 'NA', 'NA']]

        fam_m = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jck Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I23@', 'Zac Mannor', '@I12@', 'Sarah Brown', '@I10@'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I33@', 'Michael Davis', '@I13@', 'Emily Green', '@I7@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I9@', 'Eric Chen', '@I3@', 'Linda Chen', '@I11@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', ['@I2@', '@I3@', '@I4@']],
        ['@F10@', '30 Oct 2010', 'NA', '@I9@', 'Eric Chen', '@I2@', 'Jane Doe', 'NA']]

        result = gedcom_functions.noMarDes(ind_m, fam_m)
        self.assertFalse(result)

    def test5noMarDes(self):
        ind_m = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 3, False, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, False, 'NA', 'NA', 'I9'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@I10'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Daniel Kim', 'Male', '29 Apr 1998', 23, False, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, False, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, False, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Andrew Kim', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Jack Dance', 'Male', '27 Nov 1989', 32, False, 'NA', '@F5@', '@F1@'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 32, False, 'NA', 'NA', 'NA']]

        fam_m = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Zac Mannor', '@I12@', 'Sarah Brown', '@I10@'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I7@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I14@', 'Linda Chen', '@I11@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', ['@I3@']],
        ['@F10@', '30 Oct 2010', 'NA', '@I3@', 'Erica Man', '@I19@', 'Karen Wu', 'NA']]

        result = gedcom_functions.noMarDes(ind_m, fam_m)
        self.assertFalse(result)

    def test1_marriageBeforeDivorce(self):
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
        ['@F4@', '02 Apr 2005', '12 Oct 2001', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.marriageBeforeDivorce(f_mat, i_mat)
        self.assertEqual(result, ['Error: Robert Johnson was divorced before they were married.', 'Error: Linda Chen was divorced before they were married.'])

    def test2_marriageBeforeDivorce(self):
        i_mat1 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat1 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]

        result = gedcom_functions.marriageBeforeDivorce(f_mat1, i_mat1)
        self.assertEqual(result, [])

    def test3_marriageBeforeDivorce(self):
        i_mat2 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat2 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.marriageBeforeDivorce(f_mat2, i_mat2)
        self.assertEqual(result, [])

    def test4_marriageBeforeDivorce(self):
        i_mat3 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Emily Green', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat3 = [['@F1@', '18 Jan 2000', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '06 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2004', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.marriageBeforeDivorce(f_mat3, i_mat3)
        self.assertEqual(result, ['Error: Emily Green was divorced before they were married.', 'Error: Robert Johnson was divorced before they were married.', 'Error: Linda Chen was divorced before they were married.'])

    def test5_marriageBeforeDivorce(self):
        i_mat4 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Emily Green', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat4 = [['@F1@', '18 Jan 2000', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', '9 Feb 1990', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '06 Mar 2003', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2005', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.marriageBeforeDivorce(f_mat4, i_mat4)
        self.assertEqual(result, ['Error: John Smith was divorced before they were married.', 'Error: Stephanie Wong was divorced before they were married.'])

    def test1_marriageBeforeDeath(self):
        i_mat5 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat5 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.marriageBeforeDeath(f_mat5, i_mat5)
        self.assertEqual(result, [])

    def test2_marriageBeforeDeath(self):
        i_mat6 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2004', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat6 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.marriageBeforeDeath(f_mat6, i_mat6)
        self.assertEqual(result, ['Error: Robert Johnson died before they were married.'])

    def test3_marriageBeforeDeath(self):
        i_mat7 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat7 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.marriageBeforeDeath(f_mat7, i_mat7)
        self.assertEqual(result, [])

    def test4_marriageBeforeDeath(self):
        i_mat8 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1989', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat8 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.marriageBeforeDeath(f_mat8, i_mat8)
        self.assertEqual(result, ['Error: John Smith died before they were married.'])

    def test5_marriageBeforeDeath(self):
        i_mat9 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1989', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '05 Jan 2004', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat9 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.marriageBeforeDeath(f_mat9, i_mat9)
        self.assertEqual(result, ['Error: John Smith died before they were married.','Error: Robert Johnson died before they were married.'])

    def test1_olderThan150(self):
        individuals = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 151, True, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Samantha Kim', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1975', 70, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Eric Chang', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]
        result = gedcom_functions.olderThan150(individuals)
        self.assertEqual(result, ["Error: Bob Johnson should not be listed as alive."])

    def test2_olderThan150(self):
        individuals = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Stephanie Wong', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]
        result = gedcom_functions.olderThan150(individuals)
        self.assertEqual(result, [])

    def test3_olderThan150(self):
        individuals = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 78, True, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 160, True, 'NA', 'NA', '@F1@']]
        result = gedcom_functions.olderThan150(individuals)
        self.assertEqual(result, ["Error: Mary Brown should not be listed as alive."])

    def test4_olderThan150(self):
        individuals = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA']]
        result = gedcom_functions.olderThan150(individuals)
        self.assertEqual(result, [])

    def test5_olderThan150(self):
        individuals = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 151, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mary Brown', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@']]
        result = gedcom_functions.olderThan150(individuals)
        self.assertEqual(result, [])

    def test1_maleLastNames(self):
        i_mat = [['@I1@', 'John Smith', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Jane Doe', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I12@', 'Jack Harrington', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA']]  
        f_mat = [['@F1@', '18 Jan 1800', 'John Smith', '@I1@', 'John Smith', '@I11@', 'Jane Doe', ['@I12@']]]
        result = gedcom_functions.maleLastNames(i_mat, f_mat)
        self.assertEqual(result, ['Error: @I12@ does not have the same name as their father.'])

    def test2_maleLastNames(self):
        i_mat = [['@I1@', 'John Smith', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Jane Doe', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@']]  
        f_mat = [['@F1@', '18 Jan 1800', 'John Smith', '@I1@', 'John Smith', '@I11@', 'Jane Doe', 'NA']]
        result = gedcom_functions.maleLastNames(i_mat, f_mat)
        self.assertEqual(result, [])

    def test3_maleLastNames(self):
        i_mat = [['@I1@', 'John Smith', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Jane Doe', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I12@', 'Jack Harrington', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA'],
        ['@I12@', 'Joe Joe', 'F', '17 Nov 2002', 20, 'NA', '@F1@', 'NA']]  
        f_mat = [['@F1@', '18 Jan 1800', 'John Smith', '@I1@', 'John Smith', '@I11@', 'Jane Doe', ['@I12@', '@I13@']]]
        result = gedcom_functions.maleLastNames(i_mat, f_mat)
        self.assertEqual(result, ['Error: @I12@ does not have the same name as their father.'])

    def test4_maleLastNames(self):
        i_mat = [['@I1@', 'John Smith', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Jane Doe', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I12@', 'Jack Harrington', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA'],
        ['@I13@', 'Jack Harrington', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA']]  
        f_mat = [['@F1@', '18 Jan 1800', 'John Smith', '@I1@', 'John Smith', '@I11@', 'Jane Doe', ['@I12@', '@I13@']]]
        result = gedcom_functions.maleLastNames(i_mat, f_mat)
        self.assertEqual(result, ['Error: @I12@ does not have the same name as their father.', 'Error: @I13@ does not have the same name as their father.'])
        
    def test5_maleLastNames(self):
        i_mat = [['@I1@', 'John Smith', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@']]  
        f_mat = [['@F1@', '18 Jan 1800', 'John Smith', '@I1@', 'John Smith', 'NA', 'NA', 'NA']]
        result = gedcom_functions.maleLastNames(i_mat, f_mat)
        self.assertEqual(result, [])

        # Should pass and evaluate to an empty list.
    def test1_listRecentSurvivors(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, True, 'NA', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, False, '23 Feb 2023', 'NA', '@F3@'],
        ['@I5@', 'Lan Phang', 'F', '5 JUN 1925', 98, True, 'NA', 'NA', '@F3@' ]]

        family_matrix1 = [['@F1@','15 Jun 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '5 Jul 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '5 Nov 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listRecentSurvivors(individual_matrix6, family_matrix1)
        self.assertEqual(result, [])
        
    # Should pass and evaluate to Sally and Chris's Info.
    def test2_listRecentSurvivors(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, False, '14 Feb 2023', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, True, 'NA', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, True, 'NA', 'NA', '@F3@']]

        family_matrix1 = [['@F1@','15 Jun 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '5 Jul 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '5 Nov 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listRecentSurvivors(individual_matrix6, family_matrix1)
        self.assertEqual(result, [])
        
    # Should pass and evaluate to Brad and Chris's Information.
    def test3_listRecentSurvivors(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '26 Feb 2023', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, True, 'NA', 'NA', '@F3@']]

        family_matrix1 = [['@F1@','15 Jun 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '5 Jul 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '5 Nov 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listRecentSurvivors(individual_matrix6, family_matrix1)
        self.assertEqual(result, [])
        
    # Should pass and evaluate to an empty list.
    def test4_listRecentSurvivors(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, True, 'NA', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, True, 'NA', 'NA', '@F3@']]

        family_matrix1 = [['@F1@','15 Jun 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '5 Jul 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '5 Nov 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listRecentSurvivors(individual_matrix6, family_matrix1)
        self.assertEqual(result, [])
        
    # Should pass and evaluate to an empty list.
    def test5_listRecentSurvivors(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 Jun 1923', 100, True, 'NA', 'NA', '@F3@']]

        family_matrix1 = [['@F1@','15 Jun 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '5 Jul 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '5 Nov 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listRecentSurvivors(individual_matrix6, family_matrix1)
        self.assertEqual(result, [])

    # Should pass evaluate to Chris Meumann's Info.
    def test1_listRecentBirths(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '28 Mar 2023', 1, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listRecentBirths(individual_matrix6)
        self.assertEqual(result, [['@I1@','Chris Meumann', 'M', '28 Mar 2023', 1, True, 'NA', '@F1@', 'NA']])

    # Should pass and evaluate to Chris Meumann's Info.
    def test2_listRecentBirths(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '25 Mar 2023', 0, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '28 Mar 2023', 0, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listRecentBirths(individual_matrix6)
        self.assertEqual(result, [['@I1@','Chris Meumann', 'M', '25 Mar 2023', 0, True, 'NA', '@F1@', 'NA'], ['@I4@','Si Go', 'M', '28 Mar 2023', 0, True, 'NA', 'NA', '@F3@']])

    # Should pass and evaluate to an empty list.
    def test3_listRecentBirths(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listRecentBirths(individual_matrix6)
        self.assertEqual(result, [])

    # Should pass and evaluate to Chris Meumann and Si Go's Information.
    def test4_listRecentBirths(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '23 Mar 2023', 1, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '25 Mar 2023', 0, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listRecentBirths(individual_matrix6)
        self.assertEqual(result, [['@I1@','Chris Meumann', 'M', '23 Mar 2023', 1, True, 'NA', '@F1@', 'NA'], ['@I4@','Si Go', 'M', '25 Mar 2023', 0, True, 'NA', 'NA', '@F3@']])

    # Should pass and evaluate to Chris Meumann's Information
    def test5_listRecentBirths(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '27 Mar 2023', 1, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listRecentBirths(individual_matrix6)
        self.assertEqual(result, [['@I1@','Chris Meumann', 'M', '27 Mar 2023', 1, True, 'NA', '@F1@', 'NA']])

    def test1_divorceBeforeDeath(self):
        i_mat10 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1989', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, 'NA', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat10 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.divorceBeforeDeath(f_mat10, i_mat10)
        self.assertEqual(result, [])
    
    def test2_divorceBeforeDeath(self):
        i_mat11 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1989', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '11 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat11 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1990', 'NA', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.divorceBeforeDeath(f_mat11, i_mat11)
        self.assertEqual(result, ['Error: Robert Johnson died before their divorce.'])
    
    def test3_divorceBeforeDeath(self):
        i_mat12 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1988', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '11 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat12 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1980', '10 Feb 1989', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.divorceBeforeDeath(f_mat12, i_mat12)
        self.assertEqual(result, ['Error: John Smith died before their divorce.','Error: Robert Johnson died before their divorce.'])
    
    def test4_divorceBeforeDeath(self):
        i_mat13 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1988', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '13 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat13 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1980', '10 Feb 1989', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.divorceBeforeDeath(f_mat13, i_mat13)
        self.assertEqual(result, ['Error: John Smith died before their divorce.'])
    def test5_divorceBeforeDeath(self):
        i_mat14 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1990', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '13 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat14 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1980', '10 Feb 1989', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.divorceBeforeDeath(f_mat14, i_mat14)
        self.assertEqual(result, [])
    def test1_birthBeforeMP(self):
        i_mat15 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1990', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '13 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat15 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1980', '10 Feb 1989', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.birthBeforeMP(f_mat15, i_mat15)
        self.assertEqual(result, ['David Lee was born before their parents were married.'])
    def test2_birthBeforeMP(self):
        i_mat16 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1990', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '13 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 2004', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat16 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1980', '10 Feb 1989', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.birthBeforeMP(f_mat16, i_mat16)
        self.assertEqual(result, [])
    def test3_birthBeforeMP(self):
        i_mat17 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1990', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '13 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 2004', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat17 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1980', '10 Feb 1989', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2010', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2000', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1966', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.birthBeforeMP(f_mat17, i_mat17)
        self.assertEqual(result, [])

    def test4_birthBeforeMP(self):
        i_mat18 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1990', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '13 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 2004', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat18 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1980', '10 Feb 1989', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I6@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.birthBeforeMP(f_mat18, i_mat18)
        self.assertEqual(result, ['Jack Dance was born before their parents were married.'])

    def test5_birthBeforeMP(self):
        i_mat19 = [['@I1@', 'John Smith', 'Male', '23 Dec 1985', 35, True, '10 Feb 1990', '@F5@', '@F2@'],
        ['@I2@', 'Jane Doe', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Bob Johnson', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Robert Johnson', 'Male', '17 Oct 1977', 44, False, '13 October 2015', 'NA', '@F4@'],
        ['@I5@', 'David Lee', 'Male', '29 Apr 2004', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Jack Dance', 'Female', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'Mike Johnson', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Karen Lee', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Linda Chen', 'Female', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Stephanie Wong', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f_mat19 = [['@F1@', '18 Jan 2070', 'NA', '@I1@', 'Jack Dance', '@I11@', 'Jane Doe', 'NA'],
        ['@F2@', '10 Feb 1980', '10 Feb 1989', '@I1@', 'John Smith', '@10@', 'Stephanie Wong', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Mar 2002', '@I3@', 'Michael Davis', '@I13@', 'Emily Green', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Robert Johnson', '@I9@', 'Linda Chen', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Daniel Kim', '@I15@', 'Cynthia Wong', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'William Huang', '@I16@', 'Jessica Lin', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Richard Lee', '@I17@', 'Hannah Kim', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Christopher Lee', '@I18@', 'Samantha Wang', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Andrew Kim', '@I20@', 'Michelle Park', 'NA']]
        result = gedcom_functions.birthBeforeMP(f_mat19, i_mat19)
        self.assertEqual(result, [])

    def test1_listUpcomingBirthdays(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Apr 2022', 1, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listUpcomingBirthdays(individual_matrix6)
        self.assertEqual(result, ['@I1@', '@I4@'])

    def test2_listUpcomingBirthdays(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Mar 2022', 1, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '1 May 1923', 99, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listUpcomingBirthdays(individual_matrix6)
        self.assertEqual(result, ['@I4@'])
    
    def test3_listUpcomingBirthdays(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Mar 2022', 1, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '1 Jun 1923', 99, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listUpcomingBirthdays(individual_matrix6)
        self.assertEqual(result, [])

    def test4_listUpcomingBirthdays(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Mar 2022', 1, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '10 Apr 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '1 Jun 1923', 99, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listUpcomingBirthdays(individual_matrix6)
        self.assertEqual(result, [])
    
    def test5_listUpcomingBirthdays(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Mar 2022', 1, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '10 Apr 1961', 62, False, '1 Jan 2022', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '1 Jun 1923', 99, True, 'NA', 'NA', '@F3@']]

        result = gedcom_functions.listUpcomingBirthdays(individual_matrix6)
        self.assertEqual(result, [])

    def test1_listUpcomingAnniversaries(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, True, 'NA', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, False, '23 Feb 2023', 'NA', '@F3@'],
        ['@I5@', 'Lan Phang', 'F', '5 JUN 1925', 98, True, 'NA', 'NA', '@F3@' ]]

        family_matrix1 = [['@F1@','23 Jun 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '5 Jul 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '5 Nov 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listUpcomingAnniversaries(individual_matrix6, family_matrix1)
        self.assertEqual(result, [])

    def test2_listUpcomingAnniversaries(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, True, 'NA', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, False, '23 Feb 2023', 'NA', '@F3@'],
        ['@I5@', 'Lan Phang', 'F', '5 JUN 1925', 98, True, 'NA', 'NA', '@F3@' ]]

        family_matrix1 = [['@F1@','6 Sep 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '25 Sep 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '29 Apr 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listUpcomingAnniversaries(individual_matrix6, family_matrix1)
        self.assertEqual(result, [('@I5@', '@I4@')])

    def test3_listUpcomingAnniversaries(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, True, 'NA', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, False, '23 Feb 2023', 'NA', '@F3@'],
        ['@I5@', 'Lan Phang', 'F', '5 JUN 1925', 98, True, 'NA', 'NA', '@F3@' ]]

        family_matrix1 = [['@F1@','23 Apr 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '25 Sep 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '29 Apr 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listUpcomingAnniversaries(individual_matrix6, family_matrix1)
        self.assertEqual(result, [('@I5@', '@I4@')])

    def test4_listUpcomingAnniversaries(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, True, 'NA', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, False, '23 Feb 2023', 'NA', '@F3@'],
        ['@I5@', 'Lan Phang', 'F', '5 JUN 1925', 98, True, 'NA', 'NA', '@F3@' ]]

        family_matrix1 = [['@F1@','23 Nov 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '25 Sep 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '29 Dec 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listUpcomingAnniversaries(individual_matrix6, family_matrix1)
        self.assertEqual(result, [])

    def test5_listUpcomingAnniversaries(self):
        individual_matrix6 = [['@I1@','Chris Meumann', 'M', '14 Oct 2002', 20, True, 'NA', '@F1@', 'NA'],
        ['@I2@', 'Brad Meumann', 'M', '28 Jun 1961', 61, True, 'NA', '@F2@', '@F1@'],
        ['@I3@', 'Sally Go', 'F', '8 Feb 1961', 62, True, 'NA', '@F3@', '@F1@'],
        ['@I4@','Si Go', 'M', '3 May 1923', 100, False, '23 Feb 2023', 'NA', '@F3@'],
        ['@I5@', 'Lan Phang', 'F', '5 JUN 1925', 98, True, 'NA', 'NA', '@F3@' ]]

        family_matrix1 = [['@F1@','23 Nov 1985', 'NA', '@I2@', 'Brad Meumann', '@I3@', 'Sally Go',['@I1@']],
        ['@F2@', '25 Sep 1945', 'NA', '@I6@','Arthur Meumann', '@I7@', 'Lori Meumann', ['@I2@']],
        [ '@F3@', '29 Dec 1950', 'NA', '@I4@', 'Si Go', '@I5@', 'Lan Phang', ['@I3@']]]

        result = gedcom_functions.listUpcomingAnniversaries(individual_matrix6, family_matrix1)
        self.assertEqual(result, [])

# Enables us to call test file like python file.
if __name__ == '__main__':
    unittest.main()
