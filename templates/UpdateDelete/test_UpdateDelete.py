import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from subprocess import run
from test_kit.query_taker import QueryTaker
import os
import psycopg


class Manage(unittest.TestCase):
    gold = QueryTaker(os.getenv('GOLD_FILE'))
    stu = QueryTaker(os.getenv('HW_NAME'))

    @number(1)
    @weight(1)
    def test_1insert(self):
        val = self.stu.next_query(manage=True)
        self.assertTrue(val)

    @number(2)
    @weight(1)
    def test_2update(self):
        val = self.stu.next_query(manage=True)
        self.assertTrue(val)

    @number(3)
    @weight(1)
    def test_3delete(self):
        val = self.stu.next_query(manage=True)
        self.assertTrue(val)

    @number(4)
    @weight(1)
    def test_4values_insert(self):
        true = self.gold.next_query()
        self.assertEqual(str(true), "[{'dept_name': 'Cybernetics'}]")

    @number(5)
    @weight(1)
    def test_5values_update(self):
        true = self.gold.next_query()
        self.assertEqual(str(true), "[{'tot_cred': Decimal('95')}]")

    @number(6)
    @weight(1)
    def test_6values_delete(self):
        true = self.gold.next_query()
        self.assertEqual(str(true), "[]")
