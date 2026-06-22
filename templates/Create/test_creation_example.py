"""
This is the example file for testing db creation
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from subprocess import run
from test_kit.query_taker import QueryTaker
import os
import psycopg


class PsqlF(unittest.TestCase):

    gold = QueryTaker(os.getenv('GOLD_FILE'))

    @number(1)
    @weight(1)
    def test_bad(self):
        result = run("psql -U testee -h localhost -f make.sql", capture_output=True, shell=True)
        self.assertNotRegex(str(result.stderr), "ERROR")

    @number(2)
    @weight(1)
    def test_connection(self):
        connect = False
        with psycopg.connect(os.getenv('DB_URL')):
            connect = True
        self.assertTrue(connect)

    @number(3)
    @weight(1)
    def test_values(self):
        true = self.gold.next_query()
        self.assertEqual(str(true), "[{'make': 'honda'}]")
