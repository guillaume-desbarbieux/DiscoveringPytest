def list_fizz_buzz(max):
    result = []
    for i in range(1,max + 1):

        if i % 15 == 0:
            result.append("FizzBuzz")
            continue

        if i % 3 == 0:
            result.append("Fizz")
            continue

        if i % 5 == 0:
            result.append("Buzz")
            continue

        result.append(i)

    return result