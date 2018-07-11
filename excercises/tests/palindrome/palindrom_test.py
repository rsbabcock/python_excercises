import unittest
from palindrom import Palindrome

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class PalindromeTest(unittest.TestCase):

    # skip decorator, this will skip the immediate following test
    @unittest.skip("demonstrat skipping")
    def test_fun_return_8(self):
        self.assertEqual(palindrom.fun(8), 8)

    def test_is_palindrome(self):
        pal = Palindrome()
        self.assertTrue(pal.is_palindrome("Fred"))
  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()
