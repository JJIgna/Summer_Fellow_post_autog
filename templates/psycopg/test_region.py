"""
This is an example and temple
"""
# same imports as before
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from test_kit import SQLTaker
import os
# we are testing a Python file, so we need to import the file to get the function
import Region

class TestRegion(unittest.TestCase):
    # still need a QueryTaker instance for the gold file
    gold = SQLTaker(os.getenv("GOLD_FILE"))

    @weight(1)
    @number("test1")
    def test_region(self):
        val = Region.region()
        true = self.gold.next_sql()
        self.assertListEqual(val, true)
