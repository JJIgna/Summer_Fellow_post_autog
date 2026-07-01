"""
This is the template file for testing database management or update and delete statements
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from test_kit import SQLTaker
import os


class Manage(unittest.TestCase):
    gold = SQLTaker(os.getenv('GOLD_FILE'))
    stu = SQLTaker(os.getenv('HW_NAME'))

    # frist set checks students file for syntax
    @number(1)
    @weight(1)
    def test_1insert(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val)

    # next set checks contents
    @number(4)
    @weight(1)
    def test_4values_insert(self):
        true = self.gold.next_sql()
        self.assertEqual(str(true), "newly added or deleted row")
