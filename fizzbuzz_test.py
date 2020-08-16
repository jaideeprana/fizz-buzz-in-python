import fizzbuzz


def test_return_one():
    assert fizzbuzz.FizzBuzz().generate(1) == ["1"]


def test_return_one_two():
    assert fizzbuzz.FizzBuzz().generate(2) == ["1", "2"]


def test_return_one_two_fizz():
    assert fizzbuzz.FizzBuzz().generate(3) == ["1", "2", "Fizz"]


def test_return_one_two_fizz_four():
    assert fizzbuzz.FizzBuzz().generate(4) == ["1", "2", "Fizz", "4"]


def test_return_one_two_fizz_four_buzz():
    assert fizzbuzz.FizzBuzz().generate(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_return_fizzbuzz():
    assert fizzbuzz.FizzBuzz().generate(15) == ["1", "2", "Fizz", "4", "Buzz",
                                                "Fizz", "7", "8", "Fizz", "Buzz",
                                                "11", "Fizz", "13", "14", "FizzBuzz"]
