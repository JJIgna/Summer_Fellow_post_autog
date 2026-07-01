# imports
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit.SQL_taker import SQLTaker
import os
from timeout_decorator import timeout

class Assigment1(unittest.TestCase):
    # set up QueryTaker instances for both the HW and gold files
    query = SQLTaker(os.getenv('HW_NAME'))
    gold = SQLTaker(os.getenv('GOLD_FILE'))

# TESTS ARE RAN IN ALPHABETICAL ORDER NOT ORDER THEY ARE DEFINED
# THIS WILL AFFECT GRADING AS QUERIES FROM .sql FILES IS ORDER DEPENDENT

    @weight(1)
    @number("1. Department Census")
    @visibility("visible")
    @timeout(5)
    def test_Query1(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(true, out)

    @weight(1)
    @number("2. Popularity Contest")
    @visibility("hidden")
    @timeout(5)
    def test_Query2(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(true, out)

    @weight(1)
    @number("3. Hardworking")
    @visibility("visible")
    @timeout(5)
    def test_Query3(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(true, out)
