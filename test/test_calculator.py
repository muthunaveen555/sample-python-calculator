"""
This the Test program which performs unit testing on the caculator program.
Each test case generates 5 random number between 10 and 100000 and performs testing functions 
"""
import unittest
import random

# This is the class which we want to test
from app.calculator import Calculator

class Test(unittest.TestCase):
    """ 
        Basic Unittest Class which test addition, subtraction, multiplication 
        and division functions in calculator program by generating random numbers 
        between 10 and 100000 and applying respective functions
    """

    calculator_object = Calculator()
    
    def test_add(self):
        print("Testing Addition \n")
        for _ in range(5):
            num1 = random.randint(10,100000)
            num2 = random.randint(10,100000)
            answer = num1 + num2
            self.calculator_object.set_numbers(num1,num2)
            result= self.calculator_object.add()
            print(f"{num1} + {num2}:\tCalculated answer= {answer:<25} \tModule answer= {result:<25}")
            self.assertEqual(result, answer)

        print("\n Test Finished\n")

    def test_sub(self):
        print("Testing Subtraction \n")
        for _ in range(5):
            num1 = random.randint(10,100000)
            num2 = random.randint(10,100000)
            answer = num1 - num2
            self.calculator_object.set_numbers(num1,num2)
            result= self.calculator_object.sub()
            print(f"{num1} - {num2}:\tCalculated answer= {answer:<25} \tModule answer= {result:<25}")
            self.assertEqual(result, answer)

        print("\n Test Finished\n")
    
    def test_mul(self):
        print("Testing Multiplication \n")
        for _ in range(5):
            num1 = random.randint(10,100000)
            num2 = random.randint(10,100000)
            answer = num1 * num2
            self.calculator_object.set_numbers(num1,num2)
            result= self.calculator_object.mul()
            print(f"{num1} * {num2}:\tCalculated answer= {answer:<25} \tModule answer= {result:<25}")
            self.assertEqual(result, answer)

        print("\n Test finished\n")
    
    def test_div(self):
        print("Testing Division \n")
        for _ in range(5):
            num1 = random.randint(10,100000)
            num2 = random.randint(10,100000)
            answer = num1 / num2
            self.calculator_object.set_numbers(num1,num2)
            result= self.calculator_object.div()
            print(f"{num1} / {num2}:\tCalculated answer= {answer:<25} \tModule answer= {result:<25}")
            self.assertEqual(result, answer)

        try:
            print("\nTesting ZeroDivisionError\n")
            num1 = random.randint(10,100000)
            self.calculator_object.set_numbers(num1,0)
            result= self.calculator_object.div()
            print(f"{num1} / {0}:\tHandled error= {result}")
        except Exception:
            self.fail('\nunexpected exception raised')

        print("\n Test finished\n")

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
