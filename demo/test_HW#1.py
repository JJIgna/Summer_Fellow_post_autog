# imports
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit.SQL_taker import SQLTaker
import os
from timeout_decorator import timeout

class TestCaseName(unittest.TestCase):
    # set up QueryTaker instances for both the HW and gold files
    query = SQLTaker(os.getenv('HW_NAME'))
    gold = SQLTaker(os.getenv('GOLD_FILE'))

# TESTS ARE RAN IN ALPHABETICAL ORDER NOT ORDER THEY ARE DEFINED
# THIS WILL AFFECT GRADING AS QUERIES FROM .sql FILES IS ORDER DEPENDENT

    @weight(1)
    @number("1. Department Instructors")
    @visibility("visible")
    @timeout(5)
    def test_1(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(true, out)

    @weight(1)
    @number("2. Course Popularity")
    @visibility("hidden")
    @timeout(5)
    def test_2(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(true, out)

    @weight(1)
    @number("3. Instructing Time")
    @visibility("visible")
    @timeout(5)
    def test_3(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(true, out)
