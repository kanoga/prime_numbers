import unittest
from prime_number import isPrime
class PrimeTests(unittest.TestCase):
	def test_input_must_not_be_float(self):
		self.assertEqual(isPrime(10.5),"The number must be a whole number")