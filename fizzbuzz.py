class FizzBuzz:

    def generate(self, number):
        result = []
        for i in range(1, number + 1):
            result.append(self.__fizz_buzz_or_number(i))
        return result

    def __fizz_buzz_or_number(self, number):
        if self.__is_multiple_of_three_and_five(number):
            return "FizzBuzz"
        elif self.__is_multiple_of_three(number):
            return "Fizz"
        elif self.__is_multiple_of_five(number):
            return "Buzz"
        else:
            return number.__str__()

    def __is_multiple_of_three_and_five(self, number):
        return self.__is_multiple_of_three(number) and self.__is_multiple_of_five(number)

    @staticmethod
    def __is_multiple_of_three(number):
        return number % 3 == 0

    @staticmethod
    def __is_multiple_of_five(number):
        return number % 5 == 0
