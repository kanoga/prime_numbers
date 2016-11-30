import unittest
from prime_number import isPrime
class PrimeTests(unittest.TestCase):
    def test_input_must_be_a_number(self):
        self.assertEqual(isPrime(1)),"The input must be a number only")
    def test_input_must_be_a_string(self):
    	self.assertNotEqual("",(1)),"The input must not be a string")
if __name__ == "__main__":
    unittest.main()
