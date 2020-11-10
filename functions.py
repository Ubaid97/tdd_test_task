# class containing functions to be tested
class Functions:

    # function takes in two numbers. Returns True if dividing the first by the second has a remainder of 0. False otherwise
    def divisible_by(self, num1, num2):
        return num1 % num2 == 0

    # Function takes in a number. Returns True if greater than or equal to 0. False otherwise
    def positive_value(self, num):
        if num >= 0:
            return True
        else:
            return False