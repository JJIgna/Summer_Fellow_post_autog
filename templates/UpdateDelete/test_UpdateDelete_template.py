"""
This is the template file for testing database management or update and delete statements
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit.query_taker import QueryTaker
import os


class Manage(unittest.TestCase):
    gold = QueryTaker(os.getenv('GOLD_FILE'))
    stu = QueryTaker(os.getenv('HW_NAME'))

    # frist set checks students file for syntax
    @number(1)
    @weight(1)
    def test_1insert(self):
        val = self.stu.next_query(manage=True)
        self.assertTrue(val)

    # next set checks contents
    @number(4)
    @weight(1)
    def test_4values_insert(self):
        true = self.gold.next_query()
        self.assertEqual(str(true), "[{'dept_name': 'Cybernetics'}]")
