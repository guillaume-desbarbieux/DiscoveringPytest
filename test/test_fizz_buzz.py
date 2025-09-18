from src.fizz_buzz import list_fizz_buzz

def test_list_1_to_3():
    result = list_fizz_buzz(3)

    assert result ==  [1, 2, "Fizz"]

def test_list_1_to_5():
    result = list_fizz_buzz(5)

    assert result ==  [1, 2, "Fizz", 4, "Buzz"]

def test_list_1_to_15():
    result = list_fizz_buzz(15)

    assert result ==   [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

def test_list_1_to_30():
    result = list_fizz_buzz(30)
    assert result ==[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz']

    