"""
Thi is am example test file for testing privileges.
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit.SQL_taker import SQLTaker
import os

class Priv(unittest.TestCase):
    gold = SQLTaker(os.getenv('GOLD_FILE'))
    stu = SQLTaker(os.getenv('HW_NAME'))

    @number(1)
    @weight(1)
    def test_1_USER(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val, msg="error in create user statement")

    @number(2)
    @weight(1)
    def test_2_CONNECT(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val, msg="error in grant connect statement")

    @number(3)
    @weight(1)
    def test_3_SELECT(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val, msg="error in grant select statement")

    @number(4)
    @weight(1)
    def test_4_REVOKE(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val, msg="error in create revoke statement")

    @number(5)
    @weight(1)
    def test_5_role(self):
        """

        """
        true = self.gold.next_sql()
        self.assertEqual(str(true), "[{'rolname': 'alice'}]", msg="user 'alice' not found")

    @number(6)
    @weight(1)
    def test_6_connectandselect(self):
        true = self.gold.next_sql(user="alice")
        self.assertEqual(str(true), "[{'name': 'Alfaro'}]", msg="unable to access students")

    @number(7)
    @weight(1)
    def test_7values_delete(self):
        true = self.gold.next_sql(user="bob")
        self.assertFalse(true, msg="user 'bob' can still access students")
