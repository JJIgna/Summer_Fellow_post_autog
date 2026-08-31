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
    query = SQLTaker(os.getenv("HW_NAME"))
    gold = SQLTaker(os.getenv("GOLD_FILE"))

    # TESTS ARE RAN IN ALPHABETICAL ORDER NOT ORDER THEY ARE DEFINED
    # THIS WILL AFFECT GRADING AS QUERIES FROM .sql FILES IS ORDER DEPENDENT

    @weight(1)
    @number("1")
    @visibility("visible")
    @timeout(5)
    def test_Query1(self):  # ALL TESTS MUST START WITH test_
        true = self.gold.next_sql()
        out = self.query.next_sql()
        self.assertListEqual(out, true)
