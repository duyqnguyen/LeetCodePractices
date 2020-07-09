#Write a program that outputs the string representation of numbers from 1 to n.
#But for multiples of three it should output “Fizz” instead of the number and
#for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
from typing import List


class FizzBuzz:

    def __init__(self):
        self.result = []

    def FizzBuzzAlgorithm(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)

    def run(self, num):
        for x in range(1, num+1):
            self.result.append(self.FizzBuzzAlgorithm(x))
        return self.result



def main():
    # Driver code
    testInput = 15
    ourTest = FizzBuzz()
    testResult = ourTest.run(testInput)
    print("{} = {}".format(str(testInput), str(testResult)))


if __name__ == "__main__":
    main()





