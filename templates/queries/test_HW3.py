"""
This is the example file for HW using only queries in a .sql file
This is what the testing file(s) will look like
"""

# imports
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from templates.test_kit import QueryTaker
import os
import timeout_decorator

class UniDBQueries(unittest.TestCase):
    hw = os.getenv('HW_NAME')
    goldFile = os.getenv('GOLD_FILE')
    query = QueryTaker(hw)
    gold = QueryTaker(goldFile)

# CALL GOLD FILE BEFORE STUDENT FILE
# ERROR IN STUDENT FILE MAY CAUSE DESYNC FROM GOLD FILE

    @weight(1)
    @number("3.11 (a")
    @visibility("visible")
    @timeout_decorator.timeout(5)
    def test_Query1(self):
        true = str(self.gold.next_query())
        out = str(self.query.next_query())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.11 (b")
    @visibility("visible")
    @timeout_decorator.timeout(5)
    def test_Query2(self):
        true = str(self.gold.next_query())
        out = str(self.query.next_query())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.11 (c")
    @visibility("visible")
    @timeout_decorator.timeout(5)
    def test_Query3(self):
        true = str(self.gold.next_query())
        out = str(self.query.next_query())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.11 (d")
    @visibility("visible")
    @timeout_decorator.timeout(5)
    def test_Query4(self):
        true = str(self.gold.next_query())
        out = str(self.query.next_query())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.24")
    @visibility("visible")
    @timeout_decorator.timeout(5)
    def test_Query5(self):
        true = str(self.gold.next_query())
        out = str(self.query.next_query())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.25")
    @visibility("visible")
    @timeout_decorator.timeout(5)
    def test_Query6(self):
        true = str(self.gold.next_query())
        out = str(self.query.next_query())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.26")
    @visibility("visible")
    @timeout_decorator.timeout(5)
    def test_Query7(self):
        true = str(self.gold.next_query())
        out = str(self.query.next_query())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.27")
    @visibility("visible")
    @timeout_decorator.timeout(5)
    def test_Query8(self):
        true = str(self.gold.next_query())
        out = str(self.query.next_query())
        self.assertEqual(out, true)
