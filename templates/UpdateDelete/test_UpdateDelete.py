"""
This is the example file for testing database management or update and delete statements
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from test_kit.SQL_taker import SQLTaker
import os


class Manage(unittest.TestCase):
    gold = SQLTaker(os.getenv('GOLD_FILE'))
    stu = SQLTaker(os.getenv('HW_NAME'))

# -------------------------------------------------------------------------------
# Syntax check, only the student file is executed                               #
                                                                                #
    @number(1)                                                                  #
    @weight(1)                                                                  #
    def test_1insert(self):                                                     #
        val = self.stu.next_sql(manage=True)                                    #
        self.assertTrue(val, msg="error in insert statement")                   #
                                                                                #
    @number(2)                                                                  #
    @weight(1)                                                                  #
    def test_2update(self):                                                     #
        val = self.stu.next_sql(manage=True)                                    #
        self.assertTrue(val, msg="error in update statement")                   #
                                                                                #
    @number(3)                                                                  #
    @weight(1)                                                                  #
    def test_3delete(self):                                                     #
        val = self.stu.next_sql(manage=True)                                    #
        self.assertTrue(val, msg="error in delete statement")                   #
                                                                                #
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# Content check, only gold file is run                                          #
                                                                                #
    @number(4)                                                                  #
    @weight(1)                                                                  #
    def test_4values_insert(self):                                              #
        true = self.gold.next_sql()                                             #
        self.assertEqual(str(true), "[{'dept_name': 'Cybernetics'}]")           #
                                                                                #
    @number(5)                                                                  #
    @weight(1)                                                                  #
    def test_5values_update(self):                                              #
        true = self.gold.next_sql()                                             #
        self.assertEqual(str(true), "[{'tot_cred': Decimal('95')}]")            #
                                                                                #
    @number(6)                                                                  #
    @weight(1)                                                                  #
    def test_6values_delete(self):                                              #
        true = self.gold.next_sql()                                             #
        self.assertEqual(str(true), "[]")                                       #
                                                                                #
                                                                                #
# -------------------------------------------------------------------------------