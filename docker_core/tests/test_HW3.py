"""

"""

# imports
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit.query_execute import run_queries
# gold file
import os

class UniDBQueries(unittest.TestCase):
    hw = os.getenv('HW_NAME')
    goldFile = os.getenv('GOLD_FILE')
    query = run_queries(hw)
    gold = run_queries(goldFile)

    @weight(1)
    @number("3.11 (a")
    @visibility("visible")
    def test_Query1(self):
        out = str(self.query.__next__())
        true = str(self.gold.__next__())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.11 (b")
    @visibility("visible")
    def test_Query2(self):
        out = str(self.query.__next__())
        true = str(self.gold.__next__())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.11 (c")
    @visibility("visible")
    def test_Query3(self):
        out = str(self.query.__next__())
        true = str(self.gold.__next__())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.11 (d")
    @visibility("visible")
    def test_Query4(self):
        out = str(self.query.__next__())
        true = str(self.gold.__next__())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.24")
    @visibility("visible")
    def test_Query5(self):
        out = str(self.query.__next__())
        true = str(self.gold.__next__())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.25")
    @visibility("visible")
    def test_Query6(self):
        out = str(self.query.__next__())
        true = str(self.gold.__next__())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.26")
    @visibility("visible")
    def test_Query7(self):
        out = str(self.query.__next__())
        true = str(self.gold.__next__())
        self.assertEqual(out, true)

    @weight(1)
    @number("3.27")
    @visibility("visible")
    def test_Query8(self):
        out = str(self.query.__next__())
        true = str(self.gold.__next__())
        self.assertEqual(out, true)
