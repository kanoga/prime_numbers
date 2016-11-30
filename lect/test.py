import unittest
from prime_number import isPrime
class PrimeTests(unittest.TestCase):
    #test for integer
    def test_input_must_be_a_number(self):
        self.assertEqual(isPrime(1),"The input must be a number only")

    #test for negative
    def test_negative(self):
		self.assertEqual(prime_numbers.prime(-5),'This is a negative number')

    #test for alphabets 
    def test_input_must_be_a_number(self):
        self.assertEqual(isPrime("abc"),"Dont input alphabets")

   
    #test for values that are too large
    def test_input_must_be_a_number(self):
        self.assertEqual(isPrime(>1000000),"Value is too large")

    
if __name__ == "__main__":
    unittest.main()
