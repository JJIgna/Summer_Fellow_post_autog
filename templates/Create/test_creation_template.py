"""
This is the template file for the testing DB creation.
Most of the principles from the Read template apply here as well.
The main differences are running the creation file and checking the crated db.
"""

# all the imports are the same
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from subprocess import run
from test_kit.SQL_taker import SQLTaker
import os
import psycopg


# the class setup is the same
class PsqlF(unittest.TestCase):

    # you still need to make a QueryTaker instance for the gold file
    gold = SQLTaker(os.getenv('GOLD_FILE'))

    # here is where the differences begin

    # this first test is where you run the students .sql file that makes the db
    # the .sql has to go through psql to use meta commands, so the psql cmd gets ran in shell
    # and error is collected to see if any syntax errors occurs
    @number(1)
    @weight(1)
    def test_bad(self):
        result = run("psql commands goes here", capture_output=True, shell=True)
        self.assertNotRegex(str(result.stderr), "ERROR")

    # This next test tests connecting to the database.
    # this really is a glorified spell check for the name of the database
    @number(2)
    @weight(1)
    def test_connection(self):
        connect = False
        with psycopg.connect(os.getenv('DB_URL')):
            connect = True
        self.assertTrue(connect)

    # finally, all the tests in the gold file run to insure the proper data was
    #   inserted into the database
    @number(3)
    @weight(1)
    def test_values(self):
        true = self.gold.next_sql()
        self.assertEqual(str(true), "these checks will have to be hardcoded unfortunately")
