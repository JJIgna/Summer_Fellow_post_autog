"""
This is the template file for query HW using .sql files.
All the parts of the testing file will be here with places holders and explanations.

MAKE THE NAME OF THIS FILE HAS "test_" AT THE BEGINNING. THIS IS HOW unittest FINDS THE FILE.
"""

# imports
import os
import unittest

from gradescope_utils.autograder_utils.decorators import number, visibility, weight
from test_kit.SQL_taker import SQLTaker
from timeout_decorator import timeout


class TestCaseName(unittest.TestCase):
    # set up QueryTaker instances for both the HW and gold files
    query = SQLTaker(os.getenv("HW_NAME"))  # output from student file
    gold = SQLTaker(os.getenv("GOLD_FILE")) # output from goldfile

    # TESTS ARE RAN IN ALPHABETICAL ORDER NOT ORDER THEY ARE DEFINED
    # THIS WILL AFFECT GRADING AS QUERIES FROM .sql FILES IS ORDER DEPENDENT

    # select statement
    @weight(1)
    @number("1")
    @visibility("visible")
    @timeout(5)
    def test_00(self):  # ALL TESTS MUST START WITH test_
        true = self.gold.next_sql()     # output from goldfile
        out = self.query.next_sql()     # output from student file
        self.assertListEqual(out, true)

    # insert/delete
    @weight(1)
    @number("1")
    @visibility("visible")
    @timeout(5)
    def test_01(self):  # ALL TESTS MUST START WITH test_
        self.query.next_sql(manage=True) # output from student file
        true = self.gold.next_sql()      # output from goldfile
        self.assertListEqual(str(true[0]['count']), '1/0')