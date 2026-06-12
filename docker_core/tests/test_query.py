"""
test for single query
"""

# imports
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit.query_execute import run_queries
# gold file
from gold import key

class TestMany(unittest.TestCase):
    query = run_queries("many.sql")

    @weight(1)
    @number("1")
    @visibility("visible")
    def test_Query1(self):
        out = str(self.query.__next__())
        self.assertEqual(out, key[1])

    @weight(1)
    @number("2")
    @visibility("visible")
    def test_Query2(self):
        out = str(self.query.__next__())
        self.assertEqual(out, key[2])

    @weight(1)
    @number("3")
    @visibility("visible")
    def test_Query3(self):
        out = str(self.query.__next__())
        self.assertEqual(out, key[3])