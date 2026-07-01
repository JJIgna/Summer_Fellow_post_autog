# imports
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit import SQLTaker
import os
from timeout_decorator import timeout

class TestCaseName(unittest.TestCase):
    # set up QueryTaker instances for both the HW and gold files
    query = SQLTaker(os.getenv('HW_NAME'))
    gold = SQLTaker(os.getenv('GOLD_FILE'))

# TESTS ARE RAN IN ALPHABETICAL ORDER NOT ORDER THEY ARE DEFINED
# THIS WILL AFFECT GRADING AS QUERIES FROM .sql FILES IS ORDER DEPENDENT

    @weight(1)
    @number("1")
    @visibility("visible")
    @timeout(5)
    def test_1_ClassroomCapacity(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(out, true)

    @weight(1)
    @number("2")
    @visibility("visible")
    @timeout(5)
    def test_2_StudentDept(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(out, true)

    @weight(1)
    @number("3")
    @visibility("visible")
    @timeout(5)
    def test_3_Advisor(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(out, true)

    @weight(1)
    @number("3")
    @visibility("visible")
    @timeout(5)
    def test_10_Advisor(self):
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(out, true)