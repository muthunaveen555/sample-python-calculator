"""
This is the python application which performs basic calculations between two numbers
This program runs in loop unless ctrl+c is pressed
"""

class Calculator:
    """
    Class which contains functions for get user choice of operation, get numbers
    and perform addition, subtraction, multiplication and division
    """
    #choice of the operation:
    #1-Addition, 2-Subtraction, 3-Multiplication, 4-Division
    choice = -1

    #list which contains arithmetic operations name which is used in print statemen
    operations = ["ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION"]

    #numbers used for caluclations
    number1 = 0
    number2 = 0

    def get_choice(self):
        """
        get user input for choice of arithmetic operation
        this function checks for valid input and execute until user enter valid input
        """

        while True:
            try:
                self.choice = int(input("\n1.Addition\n2.Subtraction \
                            \n3.Multiplication\n4.Division\nYour choice: "))
            except ValueError:
                print("\nEnter valid number!")
                continue
            if self.choice > 4 or self.choice < 1:
                print("\nEnter number between 1 and 4!")
                continue
            print(f"\n{self.operations[self.choice-1]}")
            break

    def get_numbers(self):
        """
        get input numbers from the user
        this function checks for valid number and execute until user enters valid number
        """

        while True:
            try:
                self.number1 = float(input("\nEnter first number:"))
                self.number2 = float(input("Enter Second number:"))
            except ValueError:
                print("Sorry, Enter valid number")
                #Return to the start of the loop and prompt user input again
                continue
            else:
                #input is converted into float and ready for operations
                break

    def add(self):
        """ return sum of two numbers"""
        return self.number1+self.number2

    def sub(self):
        """ return difference of two numbers"""
        return self.number1-self.number2

    def mul(self):
        """ return multiplication of two numbers"""
        return self.number1*self.number2

    def div(self):
        """ return division of two numbers and also checks ZeroDivisionError"""
        try:
            result = self.number1/self.number2
        except ZeroDivisionError as error:
            return error
        return result

    def do_operation(self):
        """ performs the operation based on user choice """

        if self.choice == 1:
            print(f"\nOUTPUT: {calculator_object.add()}")

        elif self.choice == 2:
            print(f"\nOUTPUT: {calculator_object.sub()}")

        elif self.choice == 3:
            print(f"\nOUTPUT: {calculator_object.mul()}")

        elif self.choice == 4:
            print(f"\nOUTPUT: {calculator_object.div()}")


if __name__ == '__main__':
    calculator_object = Calculator()
    try:
        while True:
            print("\nPress CTRL+C to terminate the app!\n")
            calculator_object.get_choice()
            calculator_object.get_numbers()
            calculator_object.do_operation()
    except KeyboardInterrupt:
        print("\nApplication Closed!\n")
