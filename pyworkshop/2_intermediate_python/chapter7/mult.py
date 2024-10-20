import unittest

def multiply(x, y):
    return x * y

# Ususally test reside in a test module/seperate directory. 

class TestMultipy(unittest.TestCase):
    
    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50)

if __name__ == "__main__":
    unittest.main()