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

    # Should return an empty list.
    def test1_listOrphans(self):
        result = gedcom_functions.listOrphans([])
        self.assertEqual(result)

        # Should return...
    def test2_listOrphans(self):
        result = gedcom_functions.listOrphans([])
        self.assertEqual(result)

        # Should return...
    def test3_listOrphans(self):
        result = gedcom_functions.listOrphans([])
        self.assertEqual(result)

         # Should return...
    def test4_listOrphans(self):
        result = gedcom_functions.listOrphans([])
        self.assertEqual(result)

         # Should return...
    def test5_listOrphans(self):
        result = gedcom_functions.listOrphans([])
        self.assertEqual(result)

    # Should return an empty list.
    def test1_listLargeAgeDifferences(self):
        result = gedcom_functions.listLargeAgeDifferences([])
        self.assertEqual(result)

        # Should return...
    def test2_listLargeAgeDifferences(self):
        result = gedcom_functions.listLargeAgeDifferences([])
        self.assertEqual(result)

        # Should return...
    def test3_listLargeAgeDifferences(self):
        result = gedcom_functions.listLargeAgeDifferences([])
        self.assertEqual(result)

         # Should return...
    def test4_listLargeAgeDifferences(self):
        result = gedcom_functions.listLargeAgeDifferences([])
        self.assertEqual(result)
        
         # Should return...
    def test5_listLargeAgeDifferences(self):
        result = gedcom_functions.listLargeAgeDifferences([])
        self.assertEqual(result)

# Enables us to call test file like python file.
if __name__ == '__main__':
    unittest.main()
