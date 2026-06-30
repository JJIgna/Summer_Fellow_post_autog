"""
This is an example and temple
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from test_kit.SQL_taker import SQLTaker
import os
# we are testing a Python file, so we need to import the file to get the function
import AttTabLim

class TestRegion(unittest.TestCase):
    gold = SQLTaker(os.getenv("GOLD_FILE"))

    @weight(1)
    def test_1(self):
        val = AttTabLim.query("name", "student", 1)
        true = self.gold.next_sql()
        self.assertListEqual(val, true)

    @weight(1)
    def test_2(self):
        val = AttTabLim.query("building", "department", 4)
        true = self.gold.next_sql()
        self.assertListEqual(val, true)

    @weight(1)
    def test_3(self):
        val = AttTabLim.query("grade", "takes", 7)
        true = self.gold.next_sql()
        self.assertListEqual(val, true)

    @weight(1)
    def test_4(self):
        val = AttTabLim.query("capacity", "classroom", 9)
        true = self.gold.next_sql()
        self.assertListEqual(val, true)