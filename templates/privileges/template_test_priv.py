"""
This is a template file for testing privileges
"""

# imports should look familiar
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit.query_taker import QueryTaker
import os

# Class and function def should look familiar

class Priv(unittest.TestCase):
    gold = QueryTaker(os.getenv('GOLD_FILE'))
    stu = QueryTaker(os.getenv('HW_NAME'))

# the frist set of test will be for the student file to test syntax
    @number(1)
    @weight(1)
    def test_studentfile(self):
        val = self.stu.next_query(manage=True)
        self.assertTrue(val)

# the next set of tests will be for testing the contents of those grant and revoke statements
    @number(5)
    @weight(1)
    def test_5_role(self):
        true = self.gold.next_query()
        self.assertEqual(str(true), "This could be an expect row or assertFalse if expecting a deny")
