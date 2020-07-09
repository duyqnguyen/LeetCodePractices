#Write a program that outputs the string representation of numbers from 1 to n.
#But for multiples of three it should output “Fizz” instead of the number and
#for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
from typing import List

def run(number):

    result = []

    for x in range(1, number+1):

        if x % 3 == 0 and x % 5 == 0:
            result.append("FizzBuzz")
        elif x % 3 == 0:
            result.append("Fizz")
        elif x % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(x))

    return result


