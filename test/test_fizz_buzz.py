from src.fizz_buzz import list_fizz_buzz

def test_list_1_to_3():
    result = list_fizz_buzz(3)

    assert result ==  [1, 2, "FizzFizz"]

def test_list_1_to_5():
    result = list_fizz_buzz(5)

    assert result ==  [1, 2, "FizzFizz", 4, "BuzzBuzz"]

def test_list_1_to_15():
    result = list_fizz_buzz(15)

    assert result ==   [1, 2, 'FizzFizz', 4, 'BuzzBuzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', "Fizz", 14, 'FizzBuzzBuzz']

def test_list_1_to_30():
    result = list_fizz_buzz(30)
    assert result ==[1, 2, 'FizzFizz', 4, 'BuzzBuzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', "Fizz", 14, 'FizzBuzzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, "Fizz", 'Fizz', 'BuzzBuzz', 26, 'Fizz', 28, 29, 'FizzFizzBuzz']

def test_list_1to_100():
    result = list_fizz_buzz(100)
    assert result == [1, 2, 'FizzFizz', 4, 'BuzzBuzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 'Fizz', 14, 'FizzBuzzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 'Fizz', 'Fizz', 'BuzzBuzz', 26, 'Fizz', 28, 29, 'FizzFizzBuzz', 'Fizz', 'Fizz', 'FizzFizz', 'Fizz', 'FizzBuzzBuzz', 'FizzFizz', 'Fizz', 'Fizz', 'FizzFizz', 'Buzz', 41, 'Fizz', 'Fizz', 44, 'FizzBuzzBuzz', 46, 47, 'Fizz', 49, 'BuzzBuzz', 'FizzBuzz', 'Buzz', 'FizzBuzz', 'FizzBuzz', 'BuzzBuzz', 'Buzz', 'FizzBuzz', 'Buzz', 'Buzz', 'FizzBuzz', 61, 62, 'FizzFizz', 64, 'BuzzBuzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 'Fizz', 74, 'FizzBuzzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 'Fizz', 'Fizz', 'BuzzBuzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92, 'FizzFizz', 94, 'BuzzBuzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']

