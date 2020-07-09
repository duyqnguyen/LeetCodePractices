import unittest
import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test_number_5(self):
        solution = ['1', '2', 'Fizz', '4', 'Buzz']
        self.assertEqual(FizzBuzz.run(5), solution)

    def test_number_9(self):
        solution = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz']
        self.assertEqual(FizzBuzz.run(9), solution)

    def test_number_15(self):
        solution = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        self.assertEqual(FizzBuzz.run(15), solution)

if __name__ == '__main__':
    unittest.main()
