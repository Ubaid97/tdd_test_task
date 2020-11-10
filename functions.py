class Functions:

    def divisible_by(self, num1, num2):
        return num1 % num2 == 0

    def positive_value(self, num):
        if num >= 0:
            return True
        else:
            return False