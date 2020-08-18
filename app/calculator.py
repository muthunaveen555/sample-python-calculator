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
    #1-Addition, 2-Subtraction, 3-Multiplication, 4-Division, 5-View-history
    choice = -1

    #list which contains arithmetic operations name which is used in print statemen
    OPERATIONS = ["ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION", "HISTORY"]
    ARITHMETIC_SYMBOL = ["+", "-", "*", "/"]

    #numbers used for caluclations
    __number1 = 0
    __number2 = 0

    #current_result
    result = 0

    #constant  number of lines in history file
    MAX_LINE = 10

    def get_choice(self):
        """
        get user input for choice of arithmetic operation
        this function checks for valid input and execute until user enter valid input
        """

        while True:
            try:
                self.choice = int(input("\n1.Addition\n2.Subtraction \
                            \n3.Multiplication\n4.Division\n5.View history\nYour choice: "))
            except ValueError:
                print("\nEnter valid number!")
                continue
            if self.choice > 5 or self.choice < 1:
                print("\nEnter number between 1 and 5!")
                continue
            print(f"\n{self.OPERATIONS[self.choice-1]}")
            break

    def set_numbers(self, num1, num2):
        """setter function for numbers """

        self.__number1 = num1
        self.__number2 = num2

    def get_numbers(self):
        """
        get input numbers from the user
        this function checks for valid number and execute until user enters valid number
        """

        while True:
            try:
                self.__number1 = float(input("\nEnter first number:"))
                self.__number2 = float(input("Enter Second number:"))
            except ValueError:
                print("Sorry, Enter valid number")
                #Return to the start of the loop and prompt user input again
                continue
            else:
                #input is converted into float and ready for operations
                break

    def add(self):
        """ return sum of two numbers"""
        return self.__number1+self.__number2

    def sub(self):
        """ return difference of two numbers"""
        return self.__number1-self.__number2

    def mul(self):
        """ return multiplication of two numbers"""
        return self.__number1*self.__number2

    def div(self):
        """ return division of two numbers and also checks ZeroDivisionError"""
        try:
            result = self.__number1/self.__number2
        except ZeroDivisionError as error:
            return error
        return result

    def do_operation(self):
        """ performs the operation based on user choice """

        if self.choice == 1:
            self.get_numbers()
            self.result = self.add()
            print(f"\nOUTPUT: {self.result}")
            self.write_history()

        elif self.choice == 2:
            self.get_numbers()
            self.result = self.sub()
            print(f"\nOUTPUT: {self.result}")
            self.write_history()

        elif self.choice == 3:
            self.get_numbers()
            self.result = self.mul()
            print(f"\nOUTPUT: {self.result}")
            self.write_history()

        elif self.choice == 4:
            self.get_numbers()
            self.result = self.div()
            print(f"\nOUTPUT: {self.result}")
            self.write_history()

        elif self.choice == 5:
            self.view_history()

    def view_history(self):
        """ print last 10 calculation history """

        with open('history.txt', 'r') as file_in:
            lines = file_in.read().splitlines(True)
        for line in lines:
            print(line)

    def make_maxlines(self):
        """
            Read the history file and checks it contains only 10 lines of history
            if the number of lines become 10 then removes the old history which is first line.
        """
        with open('history.txt', 'r') as file_in:
            data = file_in.read().splitlines(True)
        if len(data) == self.MAX_LINE:
            with open('history.txt', 'w') as file_out:
                file_out.writelines(data[1:])

    def get_history_format(self):
        """ return the string format for history file"""

        symbol = self.ARITHMETIC_SYMBOL[self.choice-1]
        return f"{self.__number1} {symbol} {self.__number2} = {self.result}"

    def write_history(self):
        """ write the calculation history into history file"""
        
        self.make_maxlines()
        data = self.get_history_format()
        with open('history.txt', 'a') as file_append:
            file_append.write(f'{data}\n')

if __name__ == '__main__':
    calculator_object = Calculator()
    try:
        while True:
            print("\nPress CTRL+C to terminate the app!\n")
            calculator_object.get_choice()
            calculator_object.do_operation()
    except KeyboardInterrupt:
        print("\nApplication Closed!\n")
