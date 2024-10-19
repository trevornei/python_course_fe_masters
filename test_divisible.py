# This is where we will write our own unit tests. 

import unittest

from divisible import divisible_by

class DivisibleTestCase(unittest.TestCase):
    # Remember that the test fn's you run here need to start with "test_" naming convention to without error.
    # def test_
    def test_divisible_by(self):
        self.assertTrue(divisible_by(10, 2), True)
        self.assertFalse(divisible_by(10, 3), False)

if __name__ == "__main__":
    unittest.main()

# In the Terminal: python3 test_file.py -v
# -v == --verbose