import unittest
from prime_number import isPrime
class PrimeTests(unittest.TestCase):
    def test_input_must_be_a_number(self):
        self.assertEqual(isPrime(1),"The input must be a number only")
if __name__ == "__main__":
    unittest.main()
    def test_for_zero_number(self):
        self.assertEqual(isPrime(0), "The input must be a positive non zero number")

    def test_for_not_boolean(self):
        self.assertNotEqual(isPrime(0.5), "The input should be a whole number")
