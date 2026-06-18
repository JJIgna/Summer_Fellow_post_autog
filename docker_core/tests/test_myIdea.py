import unittest
from subprocess import run
from test_kit.query_taker import QueryTaker
import os
import psycopg



class PsqlF(unittest.TestCase):

    gold = QueryTaker(os.getenv('GOLD_FILE'))

    def test_bad(self):
        result = run("psql -U testee -h localhost -f make.sql", capture_output=True, shell=True)
        self.assertIs(result.returncode, 0)

    def test_connection(self):
        connect = False
        with psycopg.connect(os.getenv('DB_URL')):
            connect = True
        self.assertTrue(connect)

    def test_values(self):
        true = self.gold.next_query()
        self.assertEqual(str(true), "[{'name':'honda'}]")

