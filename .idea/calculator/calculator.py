class Calculator:

    def addition(self, *args):
        total = 0
        for number in args:
            total += number
        return total

    def subtraction(self, number_one, number_two):
        return number_one - number_two

    def adbbby(self, number_one, number_two):
        return sum(number_one, number_two)

    def raise_value_error(self, *args):
        return ValueError

    def gets_float(self, number_one, number_two):
        return number_one + number_two






