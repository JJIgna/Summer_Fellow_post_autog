import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from region import region
# key is a dictionary containing the correct query outputs
from gold import key

class TestRegion(unittest.TestCase):
    @weight(1)
    @number("tes1")
    def test_region(self):
        self.region = region()
        val = str(self.region)
        self.assertEqual(val, key[1])
