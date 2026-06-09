import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from region import Region

class TestRegion(unittest.TestCase):
    @weight(1)
    @number("tes1")
    def test_region(self):
        self.region = Region()
        val = str(self.region)
        self.assertEqual(val, "[{'country': 'Italy'}, {'country': 'Spai'}, {'country': 'Norway'}, {'country': 'Japa'}, {'country': 'France'}, {'country': 'USA'}, {'country': 'Netherlands'}, {'country': 'Swede'}, {'country': 'Brazil'}, {'country': 'Australia'}, {'country': 'UK'}, {'country': 'Germany'}, {'country': 'Denmark'}, {'country': 'Singapore'}, {'country': 'Canada'}, {'country': 'Finland'}]")
