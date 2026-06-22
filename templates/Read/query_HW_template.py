"""
This is the template file for query HW using .sql files.
All the parts of the testing file will be here with places holders and explanations.

MAKE THE NAME OF THIS FILE HAS "test_" AT THE BEGINNING. THIS IS HOW unittest FINDS THE FILE.

"""

"""
First we have the imports. These are very self explanatory.
    Unittest - python testing package
        this is what enable testing
    Gradescope autograder utils
        This is a set of helpful functions and decorators made by gradescope to be used with 
        their autograder
    Test.kit - custom code for testing Read
        This assists in parsing and executing Read
        QueryTaker is the class used to parse and execute
    os 
        this is used to get environment values made by the Dockerfile
    timeout_decorator
        used to timeout Read 
"""

# imports
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from test_kit import QueryTaker
import os
import timeout_decorator

"""
In unittest, a set of similar tests are defined under a class inheriting from unittest.TestCase.
Individual tests are defined using functions. 
"""

class TestCaseName(unittest.TestCase):
    class_variable = "These are available to every test under this case."
    set_up = ("If there is some set up that needs to be done for every test individually,"
              "like you need to allocate some memory, you can do so in a def setUp().")
    tear_down = ("Similarly, you make a def tearDown() that will run after every test."
                 "So, you can make a little context manager for each test.")
    hw = os.getenv('HW_NAME') # pull name of HW file from env
    goldFile = os.getenv('GOLD_FILE') # pull name of gold file from env
    # set up QueryTaker instances for both the HW and gold files
    query = QueryTaker(hw)
    gold = QueryTaker(goldFile)

# CALL GOLD FILE BEFORE STUDENT FILE
# ERROR IN STUDENT FILE MAY CAUSE DESYNC FROM GOLD FILE

# TESTS ARE RAN IN ALPHABETICAL ORDER NOT ORDER THEY ARE DEFINED
# THIS WILL AFFECT GRADING AS QUERIES FROM .sql FILES IS ORDER DEPENDENT

    @weight(1) # this is how many points the test is worth
    @number("2") # this is how gradescope orders the tests
    @visibility("visible") # this changes how students are shown the tests. here is the full list of options
                           #- `hidden`: test case will never be shown to students
                           #- `after_due_date`: test case will be shown after the assignment's due date has passed.
                           #  If late submission is allowed, then test will be shown only after the late due date.
                           #- `after_published`: test case will be shown only when the assignment is explicitly
                           #        published from the "Review Grades" page
                           #- `visible` (default): test case will always be shown
    @timeout_decorator.timeout(5) # this times out test after the given number of seconds and raises an exception
                                  #     when it does time out
    def test_Query1(self): # ALL TESTS MUST START WITH test_
        # This where you call next_query() on each file get the rows from the Read and test them
        # AGAIN, CALL GOLD BEFORE STUDENT TO AVOID DESYNC
        true = self.gold.next_query()
        out = self.query.next_query()
        self.assertDictEqual(out, true)
        """
        There are actually a lot of different assert functions available in unittest. 
        I will not list them all, but I think the most useful is assertDictEqual for testing Read.
        """
