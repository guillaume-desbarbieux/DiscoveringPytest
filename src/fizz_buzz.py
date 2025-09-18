def list_fizz_buzz(max):
    result = []
    for i in range(1,max + 1):

        result.append(fizz_buzz(i))

    return result

def fizz_buzz(number):
    fizz,buzz = count_fizz_buzz(number)

    if fizz == 0 and buzz == 0:
        return number
    else :

        return "Fizz" * fizz + "Buzz" * buzz

def count_fizz_buzz(number):
    fizz = 0
    buzz = 0

    if "3" in str(number):
        fizz += 1

    if "5" in str(number):
        buzz += 1

    if number % 3 == 0:
        fizz += 1

    if number % 5 == 0:
        buzz += 1
    return fizz,buzz


if __name__ == "__main__":
    print(list_fizz_buzz(100))