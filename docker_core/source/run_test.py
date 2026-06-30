"""
This is the run_test script. It begins the test suite. This file will never need to change.
"""

# imports
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    # grap tests
    suite = unittest.defaultTestLoader.discover('tests')
    # results.json is the file gradescope reads to pull test results
    with open('/autograder/results/results.json', 'w') as f:
        # JSONTestRunner comes from gradescope-utils and automatically creates the json file
        # with the formating gradescope is expecting
        JSONTestRunner(visibility= "visible", stream=f).run(suite)