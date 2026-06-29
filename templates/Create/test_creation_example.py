"""
This is the example file for testing db creation
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from subprocess import run
from test_kit.SQL_taker import SQLTaker
import os
import psycopg


class PsqlF(unittest.TestCase):

    gold = SQLTaker(os.getenv('GOLD_FILE'))

    @number(1)
    @weight(1)
    def test_bad(self):
        hw = os.getenv("HW_NAME")
        result = run("psql -U testee -h localhost -f" + hw, capture_output=True, shell=True)
        self.assertNotRegex(str(result.stderr), "ERROR", msg=f"syntax error in: {hw}")

    @number(2)
    @weight(1)
    def test_connection(self):
        connect = False
        with psycopg.connect(os.getenv('DB_URL')):
            connect = True
        self.assertTrue(connect, msg="connection to database failed")

    @number(3)
    @weight(1)
    def test_values(self):
        true = self.gold.next_sql()
        self.assertEqual(str(true), "[{'make': 'honda'}]")
